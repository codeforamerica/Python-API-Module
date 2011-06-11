#!/usr/bin/env python

"""Unit tests for Python API wrapper."""

import unittest

from mock import Mock

from api import api
from api import Example


def set_up_tests():
    """Cut down on boilerplate setup testing code."""
    api.API_KEY = 'fake_api_key'
    api.urlopen = Mock()
    api.json = Mock()


def called_url():
    """Test what URL was called through the mocked urlopen."""
    url = api.urlopen.call_args[0][0]
    return url


class TestExample(unittest.TestCase):

    def setUp(self):
        set_up_tests()

    def test_empty_init(self):
        example = Example()
        self.assertEquals(example.api_key, 'fake_api_key')

    def test_init_with_new_api_key(self):
        example = Example('new_api_key')
        self.assertEquals(example.api_key, 'new_api_key')

    def test_base_url(self):
        example = Example()
        self.assertEquals(example.base_url, 'http://something.web')


class TestCallApiMethod(unittest.TestCase):

    def setUp(self):
        set_up_tests()

    def test_empty_api_method_fails(self):
        example = Example()
        self.assertRaises(TypeError, example.call_api)

    def test_url_for_api_method_with_example_arg(self):
        Example().call_api('example')
        url = called_url()
        expected_url = ('http://something.web/'
                        'example?api_key=fake_api_key')
        self.assertEquals(url, expected_url)

    def test_url_for_api_method_with_kwargs(self):
        Example().call_api('example', hello='world')
        url = called_url()
        expected_url = ('http://something.web/'
                        'example?api_key=fake_api_key&hello=world')
        self.assertEquals(url, expected_url)


class TestExampleMethod(unittest.TestCase):

    def setUp(self):
        set_up_tests()

    def test_empty_example_method(self):
        Example().example()
        url = called_url()
        expected_url = ('http://something.web/'
                        'example?api_key=fake_api_key')
        self.assertEquals(url, expected_url)

    def test_example_method_with_kwargs(self):
        Example().example(foo='bar')
        url = called_url()
        expected_url = ('http://something.web/'
                        'example?api_key=fake_api_key&foo=bar')
        self.assertEquals(url, expected_url)


if __name__ == '__main__':
    unittest.main()
