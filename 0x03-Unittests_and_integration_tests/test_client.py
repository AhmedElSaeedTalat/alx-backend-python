#!/usr/bin/env python3
""" module to test access nested map"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ class to test access nested map"""
    @parameterized.expand([
        ('google',),
        ('abc',)
        ])
    def test_org(self, url: str):
        """ test org method """
        with patch('client.get_json') as mockObj:
            cls = GithubOrgClient(url)
            cls.org()
            url_used = f'https://api.github.com/orgs/{url}'
            mockObj.assert_called_once_with(url_used)
