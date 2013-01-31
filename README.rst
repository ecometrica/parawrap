================================
 Paragraph wrapping and filling
================================

The **parawrap** module is an extended version of the built-in
`textwrap`_ module. Like the standard module, it provides two
convenience functions, `wrap()`_ and `fill()`_. It also provides
``ParagraphWrapper``, which is the class that does all the work.
In addition, there is a `split()`_ function that splits up
paragraphs.

.. _wrap():

``parawrap.wrap``\(*text*\[, *width*\[, ...]])
    Wraps *text* (a string) so every line is at most *width*
    characters long. Respects paragraph breaks, which are lines
    separated by multiple newlines. Returns a list of output lines,
    without final newlines.

    Optional keyword arguments correspond to the instance attributes
    of ``ParagraphWrapper``, which mirrors ``textwrap.TextWrapper``.
    *width* defaults to 70.

.. _fill():

``parawrap.fill``\(*text*\[, *width*\[, ...]])
    Wraps *text* and returns a single string containing the wrapped
    paragraphs. ``fill()`` is shorthand for::

    "\n".join(wrap(text, ...))

    In particular, ``fill()`` accepts exactly the same keyword
    arguments as ``wrap()``.

.. _split():

``parawrap.split``\(*text*)
    Splits text into multiple paragraphs, returning a list of paragraphs.


Installation
============

To install from `PyPi`_::

    $ pip install parawrap

You can get a copy of the source by using::

    $ git clone https://github.com/ecometrica/parawrap.git

Note that this program requires Python 2.6 or higher.


Reporting bugs and submitting patches
=====================================

Please check our `issue tracker`_ for known bugs and feature requests.

We accept pull requests for fixes and new features.


Credits
=======

Simon Law wrote this program, with the generous support of Ecometrica_.

.. _textwrap: http://docs.python.org/library/textwrap.html
.. _PyPi: http://pypi.python.org/pypi/parawrap
.. _issue tracker: https://github.com/ecometrica/parawrap/issues
.. _Ecometrica: http://ecometrica.com/
