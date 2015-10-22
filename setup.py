import os
from setuptools import setup


def listify(filename):
    lines = open(filename, 'r').read().split(os.linesep)
    return filter(lambda x: x, lines)

setup(
    name='pickle_secure',
    version='0.0.0.alpha',
    url='https://github.com/spapanik/pickle-secure',
    license='GPLv2',
    description='Easily create encrypted pickle files',
    long_description=open('README.rst', 'r').read(),
    author='Stephanos Papanikolopoulos',
    author_email='spapanik21@gmail.com',
    packages=['pickle_secure'],
    keywords=['pickle', 'AES', 'secure storage'],
    install_requires=listify('requirements.txt'),
    tests_require=listify('requirements.test.txt'),
    classifiers=listify('CLASSIFIERS.txt')
)
