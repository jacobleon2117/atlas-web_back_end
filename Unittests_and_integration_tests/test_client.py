#!/usr/bin/env python3
"""
    Test_client - module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from unittest.mock import PropertyMock
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
import client


@parameterized_class(("org_payload", "repos_payload", "expected_repos", "apache2_repos"), [
    (org_payload, repos_payload, expected_repos, apache2_repos),
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
        Integration test cases for GithubOrgClient.
    """

    @classmethod
    def setUpClass(cls):
        """
            Set up the patch for requests.get before any tests run.
        """
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.mock_get_side_effect

    @classmethod
    def tearDownClass(cls):
        """
            Stop the patcher after all tests run.
        """
        cls.get_patcher.stop()

    @classmethod
    def mock_get_side_effect(cls, url, *args, **kwargs):
        """
            Define what the mock should return based on the requested URL.
        """
        if "orgs" in url:
            return cls.MockResponse(cls.org_payload)
        elif "repos" in url:
            return cls.MockResponse(cls.repos_payload)
        raise ValueError("Unmocked URL: {}".format(url))

    def test_public_repos(self, mock_json):
        """
            Test that GithubOrgClient.public_repos returns the expected repos.
        """
        mock_json.return_value = {'payload': 'success'}
        mock_name = 'client.GithubOrgClient._public_repos_url'
        with patch(mock_name,
                   new_callable=PropertyMock) as mock:
            mock.return_value = 'payload'
            test_request = client.GithubOrgClient('test')
            res = {'payload': 'success'}
            self.assertEqual(test_request.repos_payload, res)
            mock_json.assert_called_once()
            mock.assert_called_once()

    def test_apache2_repos(self):
        """
        Test that public_repos returns the expected repos for Apache2 license.
        """
        client = GithubOrgClient("apache")
        repos = client.public_repos()
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
