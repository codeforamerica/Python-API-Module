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

from api_key import API_KEY


class API(object):
    """An example class for a Python API wrapper."""

    def __init__(self, api_key=''):
        if not api_key:
            self.api_key = API_KEY
        else:
            self.api_key = api_key
        self.base_url = ''

    def call_api(self, directory, **kwargs):
        """
        A generic example api wrapping method. Other methods can use this
        method to interact with the API.
        """
        url_list = [self.base_url]
        url_list.append('/%s' % directory)
        kwargs.update({'api_key': self.api_key})
        params = urlencode(kwargs)
        url_list.extend(['?', params])
        url = ''.join(url_list)
        data = urlopen(url).read()
        # Turn JSON into a dictionary.
        return json.loads(data)
