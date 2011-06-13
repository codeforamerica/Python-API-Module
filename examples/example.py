#!/usr/bin/env python

"""Simple example API."""

from api import API

API_KEY = 'example_key'


class Example(API):

    def __init__(self, api_key=''):
        super(Example, self).__init__(api_key)
        self.base_url = 'http://something.web'
        self.output_format = 'json'
        if not self.api_key:
            self.api_key = API_KEY

    def example(self, **kwargs):
        """An example method using the api method."""
        return self.call_api('example', **kwargs)
