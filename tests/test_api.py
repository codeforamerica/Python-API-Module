#!/usr/bin/env python

import unittest

from mock import Mock

from api import api
from api import API


class TestApiClass(unittest.TestCase):

    def test_empty_api_initialization(self):
        api = API()
        self.assertEquals(api.api_key, '')
        self.assertEquals(api.base_url, '')
        self.assertEquals(api.output_format, None)

    def test_api_init_with_new_api_key(self):
        api = API('new_api_key')
        self.assertEquals(api.api_key, 'new_api_key')


class TestCallApiMethod(unittest.TestCase):

    def setUp(self):
        api.urlopen = Mock()

    def test_call_api_method(self):
        API('fake_key').call_api('example')
        expected_call = '/example?api_key=fake_key'
        api.urlopen.assert_called_with(expected_call)

    def test_call_api_method_with_kwargs(self):
        API('fake_key').call_api('example', foo='bar')
        expected_call = '/example?api_key=fake_key&foo=bar'
        api.urlopen.assert_called_with(expected_call)

    def test_call_api_method_without_output_formatting(self):
        API('fake_key').call_api('example', foo='bar', output_format=None)
        expected_call = '/example?api_key=fake_key&foo=bar'
        api.urlopen.assert_called_with(expected_call)


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


class TestXmlToDictMethod(unittest.TestCase):

    def setUp(self):
        self.xml = '<?xml version="1.0" encoding="utf-8" ?>'

    def test_simple_xml_to_dict(self):
        xml = self.xml + '<a><b>5</b><c>9</c></a>'
        expected_output = {'a': {'b': '5', 'c': '9'}}
        output = API()._xml_to_dict(xml)
        self.assertEqual(output, expected_output)

    def test_xml_to_list_of_values(self):
        xml = self.xml + '<a><b>1</b><b>2</b><b>3</b></a>'
        expected_output = {'a': {'b': ['1', '2', '3']}}
        output = API()._xml_to_dict(xml)
        self.assertEqual(output, expected_output)

    def test_xml_to_mixture_of_lists_and_dicts(self):
        xml = self.xml + '<a><b>1</b><b>2</b><c><d>3</d></c></a>'
        expected_output = {'a': {'b': ['1', '2'], 'c': {'d': '3'}}}
        output = API()._xml_to_dict(xml)
        self.assertEqual(output, expected_output)

    def test_xml_attributes_retained(self):
        xml = self.xml + '<numbers one="1" two="2" />'
        expected_output = {'numbers': {'one': '1', 'two': '2'}}
        output = API()._xml_to_dict(xml)
        self.assertEqual(output, expected_output)


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


class TestExamples(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
