#!/usr/bin/env python3
"""This module has a unit test for utils.access_nested_map"""
from parameterized import parameterized
from utils import access_nested_map, get_json
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class to test access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}},("a",), {"b": 2}),
        ({"a": {"b": 2}},("a", "b"), 2)
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
    def test_get_json(self):
        """Test get_json function"""
        self.assertEqual(get_json("http://example.com"), {"payload": True})