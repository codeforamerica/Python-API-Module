#!/usr/bin/env python

from api import API

"""Simple example API."""

class Example(API):

    def __init__(self, api_key=''):
        super(Example, self).__init__(api_key)
        self.base_url = 'http://something.web'

    def example(self, **kwargs):
        """An example method using the api method."""
        return self.call_api('example', **kwargs)
