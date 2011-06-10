Python API Template
===================

A generic template for Python API wrappers.

Current third-party libraries we're using include:

* `mock` -- Create test stubs and mocks.
<pre><code>
    >>> from mock import Mock
    >>> from api import api
    >>> api.urlopen = Mock()
</code></pre>

* `coverage` -- Check test code coverage.
<pre><code>
    $ coverage run test.py
    .................
    -----------------
    Ran 17 tests in 0.010s

    $ coverage report -m
    Name                          Stmts   Miss  Cover   Missing
    -----------------------------------------------------------
    test                            113      0   100%   
    api/__init__                      2      0   100%   
    api/api                          42      0   100%   
    api/api_key                       2      0   100%   
    -----------------------------------------------------------
    TOTAL                           159      0   100%   
</code></pre>

* `pep8` -- Check Python files are following the PEP 8 Style Guide.
<pre><code>
    $ pep8 test.py
    test.py:12:1: E302 expected 2 blank lines, found 1
</code></pre>

* `fabric` -- Adjust the directory structure accordingly to new API.
<pre><code>
    $ fab create:example_api
</code></pre>


Using Fabric
------------

The included fabfile can help reformat the `api` directory to fit the
actual API you're beginning to work on.

For example, if you're starting to write a Python wrapper for an
imaginary Census API, you could do the following:

<pre><code>
    $ fab create:census_api
</code></pre>

This will execute the commands in the `fabfile` if the `fabric` Python
library is installed on your computer. While the `fabfile` currently
performs only a few operations, it can easily be extended to include
more functionality.


Instructions
------------

1. Read through the `api` directory and tests.
2. Use `fabric` to modify the `api` directory.
3. Rewrite tests and files accordingly.


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
