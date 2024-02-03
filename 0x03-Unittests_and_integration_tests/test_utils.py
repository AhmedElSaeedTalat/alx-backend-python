#!/usr/bin/env python3
""" module to test access nested map"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Type
)


class TestAccessNestedMap(unittest.TestCase):
    """ class to test access nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: Any):
        """ test acess nested map """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         error: Type[KeyError]):
        """ test exceptions """
        with self.assertRaises(error):
            access_nested_map(nested_map, path)
