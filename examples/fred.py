#!/usr/bin/env python

"""
An example implementation of the St. Louis Federal Reserve's Economic
Data API.

FRED Documentation:  http://api.stlouisfed.org/docs/fred/
"""

from api import API


class Fred(API):
    """An easy-to-use Python wrapper over the St. Louis FRED API."""

    def __init__(self, api_key=''):
        super(Fred, self).__init__(api_key)
        self.base_url = 'http://api.stlouisfed.org/fred'
        self.output_format = 'xml'

    def _resolve_url(self, directory, child=None, **kwargs):
        """Internal method to resolve URL structure."""
        directory = [directory]
        if child:
            directory.append('/%s' % child)
        url_path = ''.join(directory)
        return self.call_api(url_path, **kwargs)

    def category(self, child=None, **kwargs):
        """
        Get a specific category.

        >>> Fred().category(category_id=125)
        """
        return self._resolve_url('category', child, **kwargs)

    def releases(self, child=None, **kwargs):
        """
        Get all releases of economic data.

        >>> Fred().releases('dates', limit=10)
        """
        return self._resolve_url('releases', child, **kwargs)

    def release(self, child=None, **kwargs):
        """
        Get a release of economic data.

        >>> Fred().release('series', release_id=51)
        """
        return self._resolve_url('release', child, **kwargs)

    def series(self, child=None, **kwargs):
        """
        Get economic series of data.

        >>> Fred().series('search', search_text="money stock")
        """
        return self._resolve_url('series', child, **kwargs)

    def sources(self, child=None, **kwargs):
        """
        Get all of FRED's sources of economic data.

        >>> Fred().sources()
        """
        return self._resolve_url('sources', child, **kwargs)

    def source(self, child=None, **kwargs):
        """
        Get a single source of economic data.

        >>> Fred().source(source_id=51)
        """
        return self._resolve_url('source', child, **kwargs)
