from setuptools import find_packages, setup

__author__ = "spapanik"
__version__ = "0.1.1"
__license__ = "GPLv2"
PKG_NAME = "pickle_secure"
PKG_SLUG = PKG_NAME.replace("_", "-")
PKG_URL = f"https://github.com/{__author__}/{PKG_SLUG}"


def contents(filename):
    with open(filename) as f:
        return f.read()


setup(
    name=PKG_NAME,
    packages=[PKG_NAME],
    version=__version__,
    license=__license__,
    description="Easily create encrypted pickle files",
    long_description=contents("readme.md"),
    author=__author__,
    author_email="spapanik21@gmail.com",
    url=PKG_URL,
    download_url=f"{PKG_URL}/tarball/{__version__}",
    python_requires=">=3.6",
    install_requires=["pycrypto>=2.6.0,<2.7.0"],
    tests_require=["pytest>=3.0.0,<4.0.0"],
    keywords=["pickle", "AES", "secure storage"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
