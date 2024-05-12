#!/usr/bin/env python3
"""This module has a unit tests for several functions"""
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock
import unittest
from client import GithubOrgClient
import requests
TEST_PAYLOAD = __import__('fixtures').TEST_PAYLOAD


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
            [{
                "repos_url": "https://api.github.com/orgs/google/repos",
                "name": "repo1"
            }]
        ),
        (
            "abc",
            [{
                "repos_url": "https://api.github.com/orgs/abc/repos",
                "name": "repo3"
            }]
        )
    ])
    @patch("client.get_json")
    def test_public_repos(self, org, payload, mock_get_json):
        "Test the GithubOrgClient.public_repos"
        mock_get_json.return_value = payload
        with patch.object(GithubOrgClient, "_public_repos_url") as mock_p:
            mock_p.return_value = payload[0]["repos_url"]
            client = GithubOrgClient(org)
            self.assertEqual(
                client.public_repos(), [repo["name"] for repo in payload]
                )
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repos, license, expected):
        """Test the GithubOrgClient.has_license"""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repos, license), expected)


@parameterized_class(
    ("org_payload", "repos_payload",
     "expected_repos", "apache2_repos"),
    [
      (
          TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1],
          TEST_PAYLOAD[0][2], TEST_PAYLOAD[0][3]
      )
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class"""
    @classmethod
    def setUpClass(cls):
        """a method that runs at the begining of the test"""
        cls.get_patcher = patch("requests.get")
        cls.mock = cls.get_patcher.start()
        cls.mock.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """"a method that runs at the end of the test"""
        cls.get_patcher.stop()

    def test_public_repo(self):
        """Test public_repo method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        # print(self.mock.call_args)

    def test_public_repos_with_license(self):
        """Test the public_repo method with licence"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
