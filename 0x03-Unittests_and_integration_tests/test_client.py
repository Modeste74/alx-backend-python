#!/usr/bin/env python3
"""Define classes for testing functions"""
import unittest
from unittest.mock import patch
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
