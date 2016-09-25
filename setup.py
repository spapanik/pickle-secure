from setuptools import setup


def listify(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def contents(filename):
    with open(filename) as f:
        return f.read()

setup(
    name='pickle_secure',
    packages=['pickle_secure'],
    version='0.0.1a0',
    description='Easily create encrypted pickle files',
    license='GPLv2',
    long_description=contents('README.txt'),
    author='Stephanos Papanikolopoulos',
    author_email='spapanik21@gmail.com',
    url='https://github.com/spapanik/pickle-secure',
    download_url='https://github.com/spapanik/pickle-secure/tarball/0.0.1a0',
    keywords=listify('KEYWORDS.txt'),
    install_requires=listify('requirements.txt'),
    tests_require=listify('requirements_test.txt'),
    classifiers=listify('CLASSIFIERS.txt'),
)
