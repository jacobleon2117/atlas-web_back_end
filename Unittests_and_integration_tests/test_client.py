#!/usr/bin/env python3
"""
    Test_client - module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

    class MockResponse:
        """
            Mock response for requests.get.
        """
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    def test_public_repos(self):
        """
        Test that GithubOrgClient.public_repos returns the expected repos.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_apache2_repos(self):
        """
        Test that public_repos returns the expected repos for Apache2 license.
        """
        client = GithubOrgClient("apache")
        repos = client.public_repos()
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
