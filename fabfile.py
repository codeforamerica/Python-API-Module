#!/usr/bin/env python

"""Fabric file to modify the `api` directory."""

from fabric.api import local


def create(name=None):
    """Create directory structure for a new API."""
    if name:
        local('mv api/ %s' % name)
        local('cd %s' % name)
        local('mv api.py %s.py' % name)
        new_init_file(name)
        local('cd ..')


def new_init_file(name):
    """Create a new `__init__.py` file."""
    content_list = ["#!/usr/bin/env python",
                    "# import classes from %s" % name,
                    "__all__ = []"]
    content_string = '\n'.join(content_list)
    local('rm __init__.py')
    local('echo %s > __init__.py' % content_string)
