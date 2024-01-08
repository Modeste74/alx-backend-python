#!/usr/bin/env python3
"""Define classes for testing functions"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """defines test for GithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """mocking get_json to avoid making actual HTTP calls"""
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.return_value = {}
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, {})

    def test_public_repos_url(self):
        """testing _public_repos_url"""
        known_payload = {"repos_url": "https://api.github.com/orgs/ex/repos"}
        with patch('client.GithubOrgClient.org') as mock_org:
            mock_org.return_value = known_payload
            client = GithubOrgClient("ex")
            with patch.object(GithubOrgClient, '_public_repos_url',
                              new_callable=PropertyMock) as mock_p:
                mock_p.return_value = known_payload["repos_url"]
                result = client._public_repos_url
                expected_url = known_payload["repos_url"]
                self.assertEqual(result, expected_url)
