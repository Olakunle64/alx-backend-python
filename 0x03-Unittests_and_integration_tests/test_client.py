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
