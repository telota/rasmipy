rasmipy
=======

Reduce Arabic strings to their rasm, i.e. remove vocalization and other
diacritics.


Usage
-----

.. code-block:: python

    >>> from rasmipy import rasmify
    >>> rasmify('الفَاتِحَة')
    'الڡاٮحه'


Installation
------------

From the Python Package Index:

    $ pip install ramsipy

From the sources:

    $ python setup.py install

With the optional REST interface:

    $ pip install rasmipy[rest-api]

REST API
--------

To run a REST service:

    $ rasmify-rest-service

Or in a Docker container (with the HTTP port mapped to 8000):

    $ docker run --rm -p 8000:80 telota/rasmify

Example GET request:

    $ curl http://localhost:8000/?text=ءَاتَيۡنَا

Example POST request:

    $ curl -H "Content-Type: text/plain" -d 'ءَاتَيۡنَا' -X POST http://localhost:8000/

There are two environment variables that can be used to configure the service:

``PORT`` defines the port that the server listens, defaults to ``8000``.
``MAX_GET_PARAMETER_LENGTH`` defines the allowed maximum length of GET requests,
defaults to ``1024``.


Resources
---------

- About the rasm writing script: https://en.wikipedia.org/wiki/Rasm
- Code repository: https://github.com/telota/rasmipy
- On the Python Package Index: https://pypi.python.org/pypi/rasmipy
- On the Docker Hub: https://hub.docker.com/r/telota/rasmify
- PHP implementation: https://packagist.org/packages/telota/rasmify
- Javascript implementation: https://github.com/telota/rasmify.js
- Javascript web demo: https://telota.github.io/rasmify.js/demo/


Contributing
------------

In order to run the tests, you need to install pytest and related packages,
preferably in a virtual environment:

.. code-block:: shell

    $ pip install -r requirements-dev.txt

Install ``rasmipy`` in an editable mode:

.. code-block:: shell

    $ python setup.py develop

Before committing changes, you should run the tests:

.. code-block:: shell

    # in the project's root directory
    $ pytest
