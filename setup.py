from setuptools import setup

__version__ = '0.1.1'
__author__ = 'spapanik'

PKG_NAME = 'pickle_secure'
PKG_URL = 'https://github.com/{author}/{pkg_slug}'.format(
    author=__author__,
    pkg_slug=PKG_NAME.replace('_', '-'),
)


def listify(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def contents(filename):
    with open(filename) as f:
        return f.read()

setup(
    name=PKG_NAME,
    packages=[PKG_NAME],
    version=__version__,
    description='Easily create encrypted pickle files',
    license='GPLv2',
    long_description=contents('README.txt'),
    author=__author__,
    author_email='spapanik21@gmail.com',
    url=PKG_URL,
    download_url='{pkg_url}/tarball/{ver}'.format(
        pkg_url=PKG_URL,
        ver=__version__,
    ),
    keywords=listify('KEYWORDS.txt'),
    install_requires=listify('requirements.txt'),
    tests_require=listify('requirements_test.txt'),
    classifiers=listify('CLASSIFIERS.txt'),
)
