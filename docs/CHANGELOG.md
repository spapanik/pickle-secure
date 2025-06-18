# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to [Semantic Versioning].

## [Unreleased]

## [0.99.9] - 2023-03-07

### Added

- Added type hints

### Removed

- Dropped python 3.7 support
- Dropped support for cryptography \<= 39.0.0

### Removed

- Removed changelog from the published wheel

## [0.9.99] - 2022-01-05

### Added

- Added python310 support
- Added a changelog

### Removed

- Dropped python36 support

## [0.9.9] - 2020-02-26

### Changed

- Fully implemented the python 3.6 pickle API

## [0.2.0] - 2018-10-06

### Changed

- Changed crypto backend from pycrypto to cryptography

## [0.1.3] - 2018-10-06

### Changed

- Changed licence to MIT

## [0.1.2] - 2018-10-06

### Removed

- Dropped support for python less than 3.6

## [0.1.1] - 2018-03-03

### Removed

- Dropped support for python 3.2

## [0.1.0] - 2018-03-03

### Added

- Initial release

## [0.0.1a1] - 2016-09-27

### Added

- Added the following constants:
    - HIGHEST_PROTOCOL
    - DEFAULT_PROTOCOL
- Added the following methods:
    - load
    - loads
    - dump
    - dumps
- Added the following exceptions:
    - PickleError
    - PicklingError
    - UnpicklingError
- Added the following classes:
    - Pickler
    - Unpickler

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
[Unreleased]: https://github.com/spapanik/pickle-secure/compare/0.99.9...master
[0.99.9]: https://github.com/spapanik/pickle-secure/compare/0.9.99...v0.99.9
[0.9.99]: https://github.com/spapanik/pickle-secure/compare/0.9.9...v0.9.99
[0.9.9]: https://github.com/spapanik/pickle-secure/compare/0.2.0...v0.9.9
[0.2.0]: https://github.com/spapanik/pickle-secure/compare/0.1.3...v0.2.0
[0.1.3]: https://github.com/spapanik/pickle-secure/compare/0.1.2...v0.1.3
[0.1.2]: https://github.com/spapanik/pickle-secure/compare/0.1.1...v0.1.2
[0.1.1]: https://github.com/spapanik/pickle-secure/compare/0.1.0...v0.1.1
[0.1.0]: https://github.com/spapanik/pickle-secure/compare/v0.0.1a1...v0.1.0
[0.0.1a1]: https://github.com/spapanik/pickle-secure/releases/tag/v0.0.1a1
