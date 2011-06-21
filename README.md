Python API Template
===================

A base class used for creating Python API wrappers.


Usage
-----

The `minimal` branch should be used as a `git submodule` when creating
new Python API wrappers. So, while development takes place on the
`master` branch, most individuals will just end up using the `minimal`
branch.

Let's make a new Python API with this in mind.

Start by creating your API directory.

    $ mkdir my_python_api && cd my_python_api
    $ touch README.md

Next, let's `git init` our new API.

    $ git init

Now we can add our `git submodule`.

    $ git submodule add -b minimal git://github.com/codeforamerica/Python-API-Template.git api

The `minimal` branch of our `Python API` should now be in the `api` directory.
We can now start on our new Python API wrapper -- let's add the
following code to `my_python_wrapper.py`.

    #!/usr/bin/env python

    """My new Python API wrapper."""

    from api import API

    class Wrapper(API):

        def __init__(self):
            super(Wrapper, self).__init__()
            self.base_url = "http://api.wrappersite.com"
            self.output_format = 'json'
            self.required_params = {'foo': 'bar'}

        def hello_world(self, **kwargs):
            """Call the `hello_world` URL path for my API."""
            self.call_api('hello_world', **kwargs)


Now, let's use our new Python API wrapper from the interactive Python
console.

    >>> from my_python_wrapper import Wrapper
    >>> wrap = Wrapper()
    >>> wrap.hello_world()
    'http://api.wrappersite.com/hello_world?foo=bar'

While the `hello_world` won't return that URL -- it will actually try to
open it with Python's `urlopen` function -- you should take a look at
the URL called. By adding the `self.required_params` to your API, those
parameters will now be used on every URL called.

Want to see something else cool? We can pass in arbitrary keywords to
our `hello_world` method, and they too will be added as URL parameters.

    >>> wrap.hello_world(api_key='my_api_key')
    'http://api.wrappersite.com/hello_world?foo=bar&api_key=my_api_key'

Again, while the `hello_world` method won't actually return this URL
string -- it will actually try to call it -- it's definitely useful to
see how the `api_key` keyword argument was added as a URL parameter.

So, what happens if instead of converting the data we're getting back
from these method calls, we really just want the intended output -- such
as `json` or `xml`?

We can do this by adding the `output_format=None` keyword argument to our
method call.

    >>> data = wrap.hello_world()
    >>> json_data = wrap.hello_world(output_format=None)

Notice how XML output is also coerced to dictionary format with the
`xml2dict` module.

    >>> wrap.output_format = 'xml'
    >>> data = wrap.hello_world()
    >>> xml_data = wrap.hello_world(output_format=None)


Third Party Libraries
---------------------

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
  * This is where you'll see how to properly subclass the `API` class.
3. Write tests and new API wrappers accordingly.


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
