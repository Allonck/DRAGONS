.. 04_beyond.rst

.. _reduce: https://dragons-recipe-system-users-manual.readthedocs.io/en/latest/reduce.html

.. _showpars: https://dragons-recipe-system-users-manual.readthedocs.io/en/latest/supptools.html#showpars

.. _show_recipes: https://dragons-recipe-system-users-manual.readthedocs.io/en/latest/supptools.html#show-recipes


.. _issues_and_limitations:

**********************
Issues and Limitations
**********************

Memory Usage
============
Some primitives use a lot of RAM memory and they can cause a crash. Memory
management in Python is notoriously difficult. The DRAGONS's team is constantly
trying to improve memory management within ``astrodata`` and the DRAGONS recipes
and primitives. If an "Out of memory" crash happens to you, if possible for your
observation sequence, try to run the pipeline on fewer images at the time,
like for each dither pattern sequence separately.

.. todo::  We need to show the user how to bring them all back together in a
    final stack at the end. This means showing what custom recipe to use and how
    to invoke it.


.. _double_messaging:

Double messaging issue
======================
If you run ``Reduce`` without setting up a logger, you will notice that the
output messages appear twice. To prevent this behaviour set up a logger.
This will send one of the output stream to a file, keeping the other on the
screen. We recommend using the DRAGONS logger located in the
:mod:`gempy.utils.logutils` module and its
:func:`~gempy.utils.logutils.config()` function:


.. code-block:: python
    :linenos:

    from gempy.utils import logutils
    logutils.config(file_name='f2_data_reduction.log')