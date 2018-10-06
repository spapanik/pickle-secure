from setuptools import setup

__version__ = "0.1.1"
__author__ = "spapanik"

PKG_NAME = "pickle_secure"
PKG_URL = "https://github.com/{author}/{pkg_slug}".format(
    author=__author__, pkg_slug=PKG_NAME.replace("_", "-")
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
    description="Easily create encrypted pickle files",
    license="GPLv2",
    long_description=contents("README.txt"),
    author=__author__,
    author_email="spapanik21@gmail.com",
    url=PKG_URL,
    download_url="{pkg_url}/tarball/{ver}".format(
        pkg_url=PKG_URL, ver=__version__
    ),
    keywords=["pickle", "AES", "secure storage"],
    install_requires=["pycrypto>=2.6.0,<2.7.0"],
    tests_require=["pytest>=3.0.0,<4.0.0"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
