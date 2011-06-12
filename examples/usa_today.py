#!/usr/bin/env python

from api import API


class Census(API):
    """Wrapper for USA Today's Census API."""

    def __init__(self, api_key=''):
        super(Census, self).__init__(api_key)
        self.base_url = 'http://api.usatoday.com/open/census'

    def _resolve_url(self, directory, keypat=None, **kwargs):
        """Internal method to resolve URL structure."""
        if keypat:
            kwargs.update({'keypat': keypat})
        return self.call_api(directory, **kwargs)

    def locations(self, keypat=None, **kwargs):
        """
        Returns all available ethnicity, housing, population and race
        information for specified area.

        >>> Census().locations()
        """
        self._resolve_url('locations', keypat, **kwargs)

    def ethnicity(self, keypat=None, **kwargs):
        """
        Returns an area's ethnic data. Information includes how much of the
        population identifies as Hispanic or non-Hispanic white, and the USA
        TODAY Diversity Index.

        >>> Census().ethnicity('CA')

        >>> Census().ethnicity('CA', sumlevid=6)
        """
        self._resolve_url('ethnicity', keypat, **kwargs)

    def housing(self, keypat=None, **kwargs):
        """
        Returns an area's housing data. Information includes the number of
        housing units, and the percentage of those that are vacant.

        >>> Census().housing('TX')

        >>> Census().housing('TX', sumlevid=3)
        """
        self._resolve_url('housing', keypat, **kwargs)

    def population(self, keypat=None, **kwargs):
        """
        Returns an area's population data. Information includes the total
        population of an area, average population per square mile, and the
        percent by which that population has changed since the last census.

        >>> Census().population()

        >>> Census().population('RI')
        """
        self._resolve_url('population', keypat, **kwargs)

    def race(self, keypat=None, **kwargs):
        """
        Returns an area's racial data. Information includes the percentage
        of an area's population that identifies as White, Black, American
        Indian, Asian, native Hawaiian/Pacific Islander, or mixed race.

        >>> Census().race()

        >>> Census().race('NY', sumlevid=3)
        """
        self._resolve_url('race', keypat, **kwargs)
