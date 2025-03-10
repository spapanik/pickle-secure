from __future__ import annotations

import pickle
from typing import TYPE_CHECKING

from pickle_secure import utils

if TYPE_CHECKING:
    from io import BufferedReader, BufferedWriter

API_VERSION = "3.6"
HIGHEST_PROTOCOL = pickle.HIGHEST_PROTOCOL
DEFAULT_PROTOCOL = pickle.DEFAULT_PROTOCOL
PickleError = pickle.PickleError
PicklingError = pickle.PicklingError
UnpicklingError = pickle.UnpicklingError


def dumps(
    obj: object, protocol: int | None = None, *, fix_imports: bool = True, key: str
) -> bytes:
    return utils.encrypt(obj, key, protocol, fix_imports=fix_imports)


def dump(
    obj: object,
    file: BufferedWriter,
    protocol: int | None = None,
    *,
    fix_imports: bool = True,
    key: str,
) -> None:
    file.write(dumps(obj, protocol=protocol, fix_imports=fix_imports, key=key))


def loads(
    bytes_object: bytes,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
    key: str,
) -> object:
    return utils.decrypt(
        bytes_object, key, fix_imports=fix_imports, encoding=encoding, errors=errors
    )


def load(
    file: BufferedReader,
    key: str,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
) -> object:
    return loads(
        file.read(), fix_imports=fix_imports, encoding=encoding, errors=errors, key=key
    )


class Pickler(pickle.Pickler):
    def __init__(
        self,
        file: BufferedWriter,
        protocol: int | None = None,
        *,
        fix_imports: bool = True,
        key: str,
    ) -> None:
        super().__init__(file, protocol, fix_imports=fix_imports)
        self.__file = file
        self.__protocol = protocol
        self.__fix_imports = fix_imports
        self.__key = key

    def dump(self, obj: object) -> None:
        return dump(
            obj,
            self.__file,
            self.__protocol,
            fix_imports=self.__fix_imports,
            key=self.__key,
        )


class Unpickler(pickle.Unpickler):
    def __init__(
        self,
        file: BufferedReader,
        *,
        fix_imports: bool = True,
        encoding: str = "ASCII",
        errors: str = "strict",
        key: str,
    ) -> None:
        super().__init__(
            file, fix_imports=fix_imports, encoding=encoding, errors=errors
        )
        self.__file = file
        self.__fix_imports = fix_imports
        self.__encoding = encoding
        self.__errors = errors
        self.__key = key

    def load(self) -> object:
        return load(
            self.__file,
            fix_imports=self.__fix_imports,
            encoding=self.__encoding,
            errors=self.__errors,
            key=self.__key,
        )
