#!/usr/bin/env python3
""" module to test access nested map"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import (
    Mapping,
    Sequence,
    Any,
    Type,
    Dict
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


class TestGetJson(unittest.TestCase):
    """ test get_json function """
    @parameterized.expand([
        ['http://example.com', {"payload": True}],
        ['http://holberton.io', {"payload": False}]
        ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mockObj: Mock):
        """ test api request function """
        mockResponse = Mock()
        expected_response = test_payload
        mockResponse.json.return_value = test_payload
        mockObj.return_value = mockResponse
        res = get_json(test_url)
        self.assertEqual(res, expected_response)
