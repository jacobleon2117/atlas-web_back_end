#!/usr/bin/env python3
"""
    test_client - Unit and Integration Tests for the GithubOrgClient Class
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
import client
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Unit tests for the GithubOrgClient class. """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, url, mock_json):
        """ 
        Test the `org` method of the GithubOrgClient class.
        
        Args:
            url (str): The name of the organization.
            mock_json (MagicMock): Mocked return value for the get_json call.
        """
        mock_json.return_value = {'login': url}  # Mocking the return value
        test_request = client.GithubOrgClient(url)
        self.assertEqual(test_request.org, mock_json.return_value)
        mock_json.assert_called_once()

    def test_public_repos_url(self):
        """ 
        Test the `_public_repos_url` property of the GithubOrgClient class.
        
        This verifies that the correct URL is returned for fetching public repositories.
        """
        mock_name = 'client.GithubOrgClient._public_repos_url'
        with unittest.mock.patch(mock_name, new_callable=PropertyMock) as mock:
            mock.return_value = {'payload': 'success'}
            test_request = client.GithubOrgClient('test')
            self.assertEqual(test_request._public_repos_url, mock.return_value)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ 
        Test the `public_repos` method of the GithubOrgClient class.
        
        Args:
            mock_json (MagicMock): Mocked return value for the get_json call.
        """
        mock_json.return_value = [{'name': 'repo1', 'license': {'key': 'my_license'}}]
        mock_name = 'client.GithubOrgClient._public_repos_url'
        
        with patch(mock_name, new_callable=PropertyMock) as mock:
            mock.return_value = 'https://api.github.com/orgs/test/repos'
            test_request = client.GithubOrgClient('test')
            repos = test_request.public_repos()
            self.assertEqual(repos, ['repo1'])  # Adjust based on your payload
            mock_json.assert_called_once()
            mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        """ 
        Test the `has_license` method of the GithubOrgClient class.
        
        Args:
            repo (dict): Repository data containing license information.
            license (str): License key to check against.
            expected (bool): Expected result of the license check.
        """
        test_client = client.GithubOrgClient('test')
        self.assertEqual(test_client.has_license(repo, license), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0], TEST_PAYLOAD[1], TEST_PAYLOAD[3], TEST_PAYLOAD[4])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration tests for the GithubOrgClient class. """

    @classmethod
    def setUpClass(cls):
        """ 
        Set up the patch for requests.get before any tests run.
        
        This is used to mock external API calls made by the client.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ 
        Stop the patcher after all tests run.
        
        Ensures no further calls are made to the mocked requests.get.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ 
        Test that the public_repos method returns the expected repositories for an organization.
        """
        self.mock_get.side_effect = self.mock_get_side_effect
        client = GithubOrgClient("google")
        repos = client.public_repos()

        self.assertEqual(repos, self.expected_repos)

    def mock_get_side_effect(self, url, *args, **kwargs):
        """ 
        Define the behavior of the mock for different URLs.
        
        This simulates API responses based on the requested URL.
        
        Args:
            url (str): The requested URL.

        Raises:
            ValueError: If the URL does not match expected patterns.
        """
        if "orgs" in url:
            return self.MockResponse(self.org_payload)
        elif "repos" in url:
            return self.MockResponse(self.repos_payload)
        raise ValueError("Unmocked URL: {}".format(url))

    class MockResponse:
        """ 
        Mock response class for simulating requests.get responses.
        
        This class provides a json method to return mock data.
        """
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data


if __name__ == '__main__':
    unittest.main()
