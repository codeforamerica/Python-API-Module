#!/usr/bin/env python

"""Thunder Chen<nkchenz@gmail.com> 2007.9.1"""

try:
    import xml.etree.ElementTree as ET
except:  # pragma: no cover
    # For Python 2.4
    import cElementTree as ET

from object_dict import object_dict
import re


class XML2Dict(object):

    def _parse_node(self, node):
        node_tree = object_dict()
        # Save attrs and text, hope there will not be a child with same name
        if node.text and node.text.strip():
            node_tree = node.text
        else:
            for k, v in node.attrib.items():
                k, v = self._namespace_split(k, v)
                node_tree[k] = v
            # Save children.
            for child in node.getchildren():
                tag, tree = self._namespace_split(child.tag, self._parse_node(child))
                if tag not in node_tree:  # the first time, so store it in dict
                    node_tree[tag] = tree
                    continue
                old = node_tree[tag]
                if not isinstance(old, list):
                    node_tree.pop(tag)
                    node_tree[tag] = [old]  # multi times, so change old dict to a list
                node_tree[tag].append(tree)  # add the new one
        if not node_tree:
            node_tree = None
        return node_tree

    def _namespace_split(self, tag, value):
        """
           Split the tag  '{http://cs.sfsu.edu/csc867/myscheduler}patients'
             ns = http://cs.sfsu.edu/csc867/myscheduler
             name = patients
        """
        result = re.compile("\{(.*)\}(.*)").search(tag)
        if result:
            value.namespace, tag = result.groups()
        return (tag, value)

    def parse(self, file):
        """Parse an XML file to a dict."""
        f = open(file, 'r')
        return self.fromstring(f.read())

    def fromstring(self, s):
        """Parse a string."""
        t = ET.fromstring(s)
        root_tag, root_tree = self._namespace_split(t.tag, self._parse_node(t))
        return object_dict({root_tag: root_tree})


class Dict2XML(object):

    def tostring(self, d):
        """convert dictionary to xml string"""
        if not isinstance(d, dict):
            raise TypeError('tostring must receive a dictionary: %r' % d)
        if len(d) != 1:
            raise ValueError('Dictionary must have exactly one root element')
        if isinstance(d.itervalues().next(), list):
            raise ValueError('Dictionary must not be a map to list: %r' % d)

        xml_list = ['<?xml version="1.0" encoding="UTF-8"?>\n']
        xml_list.append(self.__tostring_helper(d))
        return ''.join(xml_list)

    def __tostring_helper(self, d):
        if isinstance(d, int):
            return str(d)

        elif isinstance(d, basestring):
            return '<![CDATA[%s]]>' % d

        elif isinstance(d, dict):
            x = []
            for tag, content in d.iteritems():
                if content is None:
                    x.append('<%s />' % tag)
                elif isinstance(content, list):
                    for c in content:
                        if c is None:
                            x.append('<%s />' % tag)
                        else:
                            x.append('<%s>%s</%s>' %\
                                     (tag, self.__tostring_helper(c), tag))
                else:
                    x.append('<%s>%s</%s>' %\
                             (tag, self.__tostring_helper(content), tag))
            xml_string = ''.join(x)
            return xml_string

        else:
            raise ValueError('Cannot convert %r to an XML string' % d)
