#!/usr/bin/env python3
"""
    Test_client - module
"""
import unittest
import unittest.mock
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
import client
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Tests for the GithubOrgClient class. """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, url, mock_json):
        """ Test org method. """
        mock_json.return_value = {'login': url}  # Mock the return value
        test_request = client.GithubOrgClient(url)
        self.assertEqual(test_request.org, mock_json.return_value)
        mock_json.assert_called_once()

    def test_public_repos_url(self):
        """ Test public_repos method. """
        mock_name = 'client.GithubOrgClient._public_repos_url'
        with unittest.mock.patch(mock_name, new_callable=PropertyMock) as mock:
            mock.return_value = {'payload': 'success'}
            test_request = client.GithubOrgClient('test')
            self.assertEqual(test_request._public_repos_url, mock.return_value)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ Test public_repos method. """
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
        """ Test has_license method. """
        test_client = client.GithubOrgClient('test')
        self.assertEqual(test_client.has_license(repo, license), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0], TEST_PAYLOAD[1], TEST_PAYLOAD[3], TEST_PAYLOAD[4])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ GithubOrgClient integration tests. """

    @classmethod
    def setUpClass(cls):
        """ Set up the patch for requests.get before any tests run. """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ Stop the patcher after all tests run. """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test that GithubOrgClient.public_repos returns the expected repos. """
        self.mock_get.side_effect = self.mock_get_side_effect
        client = GithubOrgClient("test_org")
        repos = client.public_repos()

        self.assertEqual(repos, self.expected_repos)

    def mock_get_side_effect(self, url, *args, **kwargs):
        """ Define what the mock should return based on the requested URL. """
        if "orgs" in url:
            return self.MockResponse(self.org_payload)
        elif "repos" in url:
            return self.MockResponse(self.repos_payload)
        raise ValueError("Unmocked URL: {}".format(url))

    class MockResponse:
        """ Mock response for requests.get. """
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data


if __name__ == '__main__':
    unittest.main()
