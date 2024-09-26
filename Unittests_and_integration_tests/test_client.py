#!/usr/bin/env python3
""" 
Test module for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
import client
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """ Unit tests for the GithubOrgClient class. """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_json):
        """ 
        Test that GithubOrgClient.org returns the correct value.
        """
        test_request = client.GithubOrgClient(org)
        mock_json.return_value = {"login": org}
        
        # Access the org property
        self.assertEqual(test_request.org, mock_json.return_value)
        mock_json.assert_called_once_with(f'https://api.github.com/orgs/{org}')

    def test_public_repos_url(self):
        """ 
        Test GithubOrgClient._public_repos_url returns the expected URL.
        """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': 'https://api.github.com/orgs/test/repos'}
            test_request = client.GithubOrgClient('test')
            
            expected_url = 'https://api.github.com/orgs/test/repos'
            self.assertEqual(test_request._public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ 
        Test that GithubOrgClient.public_repos returns the expected repos.
        """
        mock_json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
        
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_url.return_value = 'https://api.github.com/orgs/test/repos'
            test_request = client.GithubOrgClient('test')
            repos = test_request.public_repos()
            
            expected_repos = [{'name': 'repo1'}, {'name': 'repo2'}]
            self.assertEqual(repos, expected_repos)
            mock_json.assert_called_once()
            mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ 
        Test that GithubOrgClient.has_license correctly identifies the license.
        """
        test_client = client.GithubOrgClient('test')
        self.assertEqual(test_client.has_license(repo, license_key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(org_payload, repos_payload, expected_repos, apache2_repos)]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration tests for the GithubOrgClient class. """

    @classmethod
    def setUpClass(cls):
        """ Set up test class with mocked requests.get. """
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = cls.mock_get_side_effect

    @classmethod
    def tearDownClass(cls):
        """ Stop the patcher after all tests run. """
        cls.get_patcher.stop()

    @classmethod
    def mock_get_side_effect(cls, url, *args, **kwargs):
        """ Define the mock return values based on the requested URL. """
        if "orgs" in url:
            return cls.MockResponse(cls.org_payload)
        elif "repos" in url:
            return cls.MockResponse(cls.repos_payload)
        raise ValueError("Unmocked URL: {}".format(url))

    class MockResponse:
        """ Mock response for requests.get. """
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    def test_public_repos(self):
        """ Test that GithubOrgClient.public_repos returns the expected repos. """
        client = client.GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_apache2_repos(self):
        """ Test that public_repos returns the expected repos for Apache2 license. """
        client = client.GithubOrgClient("apache")
        repos = client.public_repos()
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
