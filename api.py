#!/usr/bin/env python

"""Python wrapper for an API."""

try:
    import json
except ImportError:  # pragma: no cover
    # For older versions of Python.
    import simplejson as json

try:
    from urllib import urlencode
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.parse import urlencode

try:
    from urllib2 import urlopen
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.request import urlopen

from xml2dict import xml2dict


class API(object):
    """An example class for a Python API wrapper."""

    def __init__(self, api_key=''):
        if api_key:
            self.api_key = api_key
        self.base_url = ''
        self.output_format = None
        self.required_params = None

    def call_api(self, directory=None, **kwargs):
        """
        A generic example api wrapping method. Other methods can use this
        method to interact with the API.
        """
        self._check_base_url()
        url_list = [self.base_url]
        if directory:
            url_list.append('/%s' % directory)
        if self.required_params:
            kwargs.update(self.required_params)
        try:
            output_format = kwargs.pop('output_format')
        except KeyError:
            output_format = self.output_format
        if kwargs:
            params = urlencode(kwargs)
            url_list.extend(['?', params])
        url = ''.join(url_list)
        data = urlopen(url).read()
        return self._format_data(output_format, data)

    def _check_base_url(self):
        """Internal method to format `self.base_url`."""
        base_url = self.base_url
        if base_url and base_url.endswith('/'):
            base_url = base_url.rstrip('/')
            self.base_url = base_url

    def _format_data(self, output_format, data):
        """Internal method to return formatted data to developer."""
        if output_format:
            # Check for cases people capitalize JSON or XML.
            output_format =  output_format.lower()
        if output_format == 'json':
            # Turn JSON into a dictionary.
            return json.loads(data)
        elif output_format == 'xml':
            return self._xml_to_dict(data)
        return data

    def _xml_to_dict(self, xml):
        """
        Internal method to turn XML to dictionary output. Developers can
        overwrite this method to use their favorite XML parser of choice.
        """
        return xml2dict(xml)
