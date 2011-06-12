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


Instructions
------------

1. Read through the `api` and `tests` directories.
2. Read through files in the `examples` directory.
3. Write tests and new API wrappers accordingly.


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
