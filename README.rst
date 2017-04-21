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


Resources
---------

- About the rasm writing script: https://en.wikipedia.org/wiki/Rasm
- Code repository: https://github.com/telota/rasmipy
- On the Python Package Index: https://pypi.python.org/pypi/rasmipy
- PHP implementation: https://packagist.org/packages/telota/rasmify
- Javascript implementation: https://github.com/telota/rasmify.js
- Web demo: https://telota.github.io/rasmify.js/demo/


Contributing
------------

In order to run the tests, you need to install pytest and related packages,
preferably in a virtual environment:

    $ pip install -r requirements-dev.txt

Install ``rasmipy`` in an editable mode:

    $ python setup.py develop

Before committing changes, you should run the tests:

    # in the project's root directory
    $ pytest
