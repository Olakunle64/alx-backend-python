#!/usr/bin/env python3
"""This module has a unit tests for several functions"""
from parameterized import parameterized
from unittest.mock import patch, Mock
import unittest
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient Class to test test_org function"""
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    @patch("client.get_json")
    def test_org(self, org, expected, mock_get_json):
        """Test the GithubOrgClient.org"""
        mock_obj = Mock()
        mock_obj.return_value = expected
        mock_get_json.return_value = mock_obj
        client = GithubOrgClient(org)
        self.assertEqual(client.org(), expected)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
            )

    @parameterized.expand([
        ("google", {"payload": False})
    ])
    @patch.object(GithubOrgClient, "_public_repos_url")
    def test_public_repos_url(self, org, payload, mock_p_repos_url):
        "Test the GithubOrgClient._public_repos_url method"
        mock_p_repos_url.return_value = payload
        client = GithubOrgClient(org)
        self.assertEqual(client._public_repos_url(), payload)
