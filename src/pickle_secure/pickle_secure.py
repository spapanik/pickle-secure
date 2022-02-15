import pickle
from io import BytesIO
from typing import Any

from pickle_secure import utils

API_VERSION = "3.6"
HIGHEST_PROTOCOL = pickle.HIGHEST_PROTOCOL
DEFAULT_PROTOCOL = pickle.DEFAULT_PROTOCOL
PickleError = pickle.PickleError
PicklingError = pickle.PicklingError
UnpicklingError = pickle.UnpicklingError


def dumps(
    obj: Any, protocol: int = None, *, fix_imports: bool = True, key: str
) -> bytes:
    return utils.encrypt(obj, key, protocol, fix_imports)


def dump(
    obj: Any, file: BytesIO, protocol: int = None, *, fix_imports: bool = True, key: str
) -> None:
    file.write(dumps(obj, protocol=protocol, fix_imports=fix_imports, key=key))


def loads(
    bytes_object: bytes,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
    key: str,
) -> Any:
    return utils.decrypt(bytes_object, key, fix_imports, encoding, errors)


def load(
    file: BytesIO,
    key: str,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
) -> Any:
    return loads(
        file.read(), fix_imports=fix_imports, encoding=encoding, errors=errors, key=key
    )


class Pickler(pickle.Pickler):
    def __init__(
        self, file: BytesIO, protocol: int = None, *, fix_imports: bool = True, key: str
    ):
        super().__init__(file, protocol, fix_imports=fix_imports)
        self.__file = file
        self.__protocol = protocol
        self.__fix_imports = fix_imports
        self.__key = key

    def dump(self, obj: Any) -> None:
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
        file: BytesIO,
        *,
        fix_imports: bool = True,
        encoding: str = "ASCII",
        errors: str = "strict",
        key: str,
    ):
        super().__init__(
            file, fix_imports=fix_imports, encoding=encoding, errors=errors
        )
        self.__file = file
        self.__fix_imports = fix_imports
        self.__encoding = encoding
        self.__errors = errors
        self.__key = key

    def load(self) -> Any:
        return load(
            self.__file,
            fix_imports=self.__fix_imports,
            encoding=self.__encoding,
            errors=self.__errors,
            key=self.__key,
        )
