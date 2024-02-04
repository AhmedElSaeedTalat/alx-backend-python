#!/usr/bin/env python3
""" module to test access nested map"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ class to test access nested map"""
    @parameterized.expand([
        ('google',),
        ('abc',)
        ])
    @patch('client.get_json')
    def test_org(self, url: str, mockObj: Mock):
        """ test org method to check if get_json was called """
        cls = GithubOrgClient(url)
        cls.org()
        url_used = f'https://api.github.com/orgs/{url}'
        mockObj.assert_called_once_with(url_used)

    def test_public_repos_url(self):
        """ mock property from org as returned value """
        target = 'client.GithubOrgClient.org'
        with patch(target, new_callable=PropertyMock) as propMock:
            value = {'repos_url': 'value'}
            propMock.return_value = value
            cls = GithubOrgClient(value['repos_url'])
            result = cls._public_repos_url
            self.assertEqual(result, value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_getJson: Mock):
        """ test public repos """
        payLoad = [{'name': 'repo'}, {'name': 'second_repo'}]
        mock_getJson.return_value = payLoad
        target = 'client.GithubOrgClient._public_repos_url'
        with patch(target, new_callable=PropertyMock) as _reposMock:
            _reposMock.return_value = 'repo'

            Github = GithubOrgClient('repo')
            result_list = Github.public_repos()
            self.assertEqual(result_list, ['repo', 'second_repo'])
            mock_getJson.assert_called_once()
            _reposMock.assert_called_once()
