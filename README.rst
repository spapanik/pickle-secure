================================
pickle-secure: encrypted pickles
================================

.. image:: https://github.com/spapanik/pickle-secure/actions/workflows/build.yml/badge.svg
  :alt: Build
  :target: https://github.com/spapanik/pickle-secure/actions/workflows/build.yml
.. image:: https://img.shields.io/github/license/spapanik/pickle-secure
  :alt: License
  :target: https://github.com/spapanik/pickle-secure/blob/main/LICENSE.txt
.. image:: https://img.shields.io/pypi/v/pickle-secure
  :alt: PyPI
  :target: https://pypi.org/project/pickle-secure
.. image:: https://pepy.tech/badge/pickle-secure
  :alt: Downloads
  :target: https://pepy.tech/project/pickle-secure
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :alt: Code style
  :target: https://github.com/psf/black

``pickle-secure`` is a wrapper around pickle that creates encrypted pickles.

In a nutshell
-------------

Installation
^^^^^^^^^^^^

The easiest way is to use `poetry`_ to manage your dependencies and add *pickle-secure* to them.

.. code-block:: toml

    [tool.poetry.dependencies]
    pickle-secure = "^0.9.0"

Usage
^^^^^

``pickle-secure`` offers a similar API as the built-in pickle.

Links
-----

- `Documentation`_
- `Changelog`_


.. _poetry: https://python-poetry.org/
.. _Changelog: https://github.com/spapanik/pickle-secure/blob/main/CHANGELOG.rst
.. _Documentation: https://pickle-secure.readthedocs.io/en/latest/
