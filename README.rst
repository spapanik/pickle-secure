================================
pickle-secure: encrypted pickles
================================

.. image:: https://github.com/spapanik/pickle-secure/actions/workflows/tests.yml/badge.svg
  :alt: Tests
  :target: https://github.com/spapanik/pickle-secure/actions/workflows/tests.yml
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
  :alt: code style: black
  :target: https://github.com/psf/black
.. image:: https://img.shields.io/badge/build%20automation-yamk-success
  :alt: build automation: yam
  :target: https://github.com/spapanik/yamk
.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json
  :alt: Lint: ruff
  :target: https://github.com/charliermarsh/ruff

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
