#!/usr/bin/env python

"""Unit tests for the xml2dict module."""

import unittest

import api
from api.xml2dict import xml2dict

# XML Strings
import xml_strings


class TestXML2Dict(unittest.TestCase):

    def setUp(self):
        self.xml = '<?xml version="1.0" encoding="utf-8" ?>'

    def test_simple_xml_to_dict(self):
        xml = self.xml + '<a><b>5</b><c>9</c></a>'
        expected_output = {'a': {'b': '5', 'c': '9'}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_xml_to_list_of_values(self):
        xml = self.xml + '<a><b>1</b><b>2</b><b>3</b></a>'
        expected_output = {'a': {'b': ['1', '2', '3']}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_xml_to_mixture_of_lists_and_dicts(self):
        xml = self.xml + '<a><b>1</b><b>2</b><c><d>3</d></c></a>'
        expected_output = {'a': {'b': ['1', '2'], 'c': {'d': '3'}}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_xml_attributes_retained(self):
        xml = self.xml + '<numbers one="1" two="2" />'
        expected_output = {'numbers': {'one': '1', 'two': '2'}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_both_attributes_and_child_nodes(self):
        xml = self.xml + '<a foo="foo">bar</a>'
        expected_output = {'a': {'a': 'bar', 'foo': 'foo'}}
        self.assertEqual(xml2dict(xml), expected_output)

    def test_error_raised_when_passed_complicated_XML(self):
        xml = self.xml + '<tag tag="foo">bar</tag>'
        self.assertRaises(ValueError, xml2dict, xml)

    def test_against_XML_namespaces(self):
        xml = self.xml + xml_strings.namespaces_table
        expected_output = {
            ('http://www.w3.org/TR/html4/', 'table'): {
                ('http://www.w3.org/TR/html4/', 'tr'): {
                    ('http://www.w3.org/TR/html4/', 'td'): ['Apples', 'Bananas']
                }
            }
        }
        self.assertEquals(xml2dict(xml), expected_output)

    def test_node_attribute_has_same_name_as_child(self):
        xml = self.xml + '<a b="foo"><b><c>1</c></b></a>'
        expected_output = {'a': {'b': ['foo', {'c': '1'}]}}
        self.assertEquals(xml2dict(xml), expected_output)


if __name__ == '__main__':
    unittest.main()
