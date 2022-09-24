Usage
=====

.. _installation:

Installation
------------

To use Test1, install minimal python 3.8:

.. code-block:: console

    $ sudo apt-get install python3

Calculate Fibonacci
-------------------

The Test1 CLI calculates the fibonacci number, using the private ``test1.fibonacci._fibo()`` function:

.. autofunction:: test1.fibonacci._fibo
    :noindex:

.. code-block:: python

    >>> from test1.fibonacci import _fibo
    >>> _fibo(5, -1)
    13