#!/usr/bin/env python3
"""defines unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """defines test for certain modules"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """tests whether the function acsess_nested_map
        return what its supposed to return"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)