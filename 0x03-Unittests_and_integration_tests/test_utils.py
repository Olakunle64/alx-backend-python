#!/usr/bin/env python3
"""This module has a unit test for utils.access_nested_map"""
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch, Mock
import requests


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class to test access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access_nested_map function with exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class to test get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url, expected, mock_object):
        """Test get_json function"""
        my_mock = Mock()
        my_mock.json.return_value = expected
        mock_object.return_value = my_mock
        self.assertEqual(get_json(url), expected)
        mock_object.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """TestMomoize class to test memoize function"""
    def test_memoize(self):
        """Test memoize function"""
        class TestClass:
            """Class"""
            def a_method(self):
                """a_method"""
                return 42

            @memoize
            def a_property(self):
                """a_property"""
                return self.a_method()
        with patch.object(TestClass, "a_method") as mock_a_method:
            mock_a_method.return_value = 42
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_a_method.assert_called_once()
