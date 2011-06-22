#!/usr/bin/env python

import unittest

from mock import Mock

import api
from api import API


class TestApiClass(unittest.TestCase):

    def test_empty_api_initialization(self):
        my_api = API()
        self.assertEquals(my_api.base_url, '')
        self.assertEquals(my_api.output_format, None)
        self.assertEquals(my_api.required_params, None)

    def test_api_init_with_new_api_key(self):
        my_api = API('new_api_key')
        self.assertEquals(my_api.api_key, 'new_api_key')


class TestCallApiMethod(unittest.TestCase):

    def setUp(self):
        api.urlopen = Mock()

    def test_call_api_method(self):
        API('fake_key').call_api('example')
        expected_call = '/example'
        api.urlopen.assert_called_with(expected_call)

    def test_call_api_method_with_kwargs(self):
        API('fake_key').call_api('example', foo='bar')
        expected_call = '/example?foo=bar'
        api.urlopen.assert_called_with(expected_call)

    def test_call_api_method_without_output_formatting(self):
        API('fake_key').call_api('example', foo='bar', output_format=None)
        expected_call = '/example?foo=bar'
        api.urlopen.assert_called_with(expected_call)

    def test_call_api_method_with_required_params(self):
        my_api = API('fake_key')
        my_api.required_params = {'api_key': my_api.api_key}
        my_api.call_api('example', foo='bar')
        expected_call = '/example?api_key=fake_key&foo=bar'
        api.urlopen.assert_called_with(expected_call)


class TestCheckBaseUrlMethod(unittest.TestCase):

    def test_url_without_trailing_slash(self):
        api = API()
        api.base_url = 'http://mysite.com'
        api._check_base_url()
        self.assertEquals(api.base_url, 'http://mysite.com')

    def test_url_with_trailing_slash(self):
        api = API()
        api.base_url = 'http://mysite.com/'
        api._check_base_url()
        self.assertEquals(api.base_url, 'http://mysite.com')


class TestFormatDataMethod(unittest.TestCase):

    def test_json_output(self):
        data = '{"a": {"b": "c"}}'
        output = API()._format_data('json', data)
        expected_output = {'a': {'b': 'c'}}
        self.assertEquals(output, expected_output)

    def test_xml_output(self):
        data = ('<?xml version="1.0" encoding="utf-8" ?>'
                '<a><b>c</b></a>')
        output = API()._format_data('xml', data)
        expected_output = {'a': {'b': 'c'}}
        self.assertEquals(output, expected_output)

    def test_without_formatting_output(self):
        data = "ohai, I'm data"
        output = API()._format_data(None, data)
        self.assertEquals(output, data)


class ExampleJson(API):

    def __init__(self, api_key=''):
        super(ExampleJson, self).__init__(api_key)
        self.base_url = 'http://example.com'
        self.output_format = 'json'
        self.api_key = 'json_api_key'


class ExampleXml(API):

    def __init__(self, api_key=''):
        super(ExampleXml, self).__init__(api_key)
        self.base_url = 'http://example.com'
        self.output_format = 'xml'
        self.api_key = 'xml_api_key'


class ExampleKeywords(API):

    def __init__(self):
        super(ExampleKeywords, self).__init__()
        self.base_url = 'http://example.com'
        self.output_format = 'json'
        self.required_params = {'foo': 'bar'}


class TestExamples(unittest.TestCase):

    def setUp(self):
        api.urlopen = Mock()
        api.json = Mock()

    def tearDown(self):
        import json
        api.json = json

    def test_example_json_api(self):
        example = ExampleJson()
        self.assertEquals(example.api_key, 'json_api_key')
        self.assertEquals(example.base_url, 'http://example.com')
        self.assertEquals(example.output_format, 'json')

    def test_example_xml_api(self):
        example = ExampleXml()
        self.assertEquals(example.api_key, 'xml_api_key')
        self.assertEquals(example.base_url, 'http://example.com')
        self.assertEquals(example.output_format, 'xml')

    def test_example_with_new_required_params(self):
        example = ExampleKeywords()
        example.call_api('test')
        expected_url = 'http://example.com/test?foo=bar'
        api.urlopen.assert_called_with(expected_url)


if __name__ == '__main__':
    unittest.main()
