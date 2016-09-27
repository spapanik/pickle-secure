from setuptools import setup

PKG_NAME = 'pickle_secure'
__version__ = '0.0.1a1'


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
    author='Stephanos Papanikolopoulos',
    author_email='spapanik21@gmail.com',
    url='https://github.com/spapanik/{pkg_name}'.format(pkg_name=PKG_NAME),
    download_url='https://github.com/spapanik/{pkg_name}/tarball/{ver}'.format(
        pkg_name=PKG_NAME,
        ver=__version__,
    ),
    keywords=listify('KEYWORDS.txt'),
    install_requires=listify('requirements.txt'),
    tests_require=listify('requirements_test.txt'),
    classifiers=listify('CLASSIFIERS.txt'),
)
