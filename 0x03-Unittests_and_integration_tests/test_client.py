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

    @parameterized.expand([
        (
            "google",
            {"repos_url": "https://api.github.com/orgs/google/repos"},
            [{"name": "repo1"}, {"name": "repo2"}]
        ),
        (
            "abc",
            {"repos_url": "https://api.github.com/orgs/abc/repos"},
            [{"name": "repo1"}, {"name": "repo2"}]
        )
    ])
    @patch("client.get_json")
    def test_public_repos(self, org, payload, repos_list, mock_get_json):
        "Test the GithubOrgClient.public_repos"
        with patch.object(GithubOrgClient, "_public_repos_url") as mock_p:
            mock_p.return_value = payload
            mock_get_json.return_value = repos_list
            client = GithubOrgClient(org)
            self.assertEqual(
                client.public_repos(), [repo["name"] for repo in repos_list]
                )
            mock_get_json.assert_called_once()
