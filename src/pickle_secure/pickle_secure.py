import pickle

from pickle_secure import utils

API_VERSION = "3.6"
HIGHEST_PROTOCOL = pickle.HIGHEST_PROTOCOL
DEFAULT_PROTOCOL = pickle.DEFAULT_PROTOCOL
PickleError = pickle.PickleError
PicklingError = pickle.PicklingError
UnpicklingError = pickle.UnpicklingError


def dumps(obj, protocol=None, *, fix_imports=True, key):
    return utils.encrypt(obj, key, protocol, fix_imports)


def dump(obj, file, protocol=None, *, fix_imports=True, key):
    file.write(dumps(obj, protocol=protocol, fix_imports=fix_imports, key=key))


def loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict", key):
    return utils.decrypt(bytes_object, key, fix_imports, encoding, errors)


def load(file, key, *, fix_imports=True, encoding="ASCII", errors="strict"):
    return loads(
        file.read(), fix_imports=fix_imports, encoding=encoding, errors=errors, key=key
    )


class Pickler(pickle.Pickler):
    def __init__(self, file, protocol=None, *, fix_imports=True, key):
        super().__init__(file, protocol, fix_imports=fix_imports)
        self.__file = file
        self.__protocol = protocol
        self.__fix_imports = fix_imports
        self.__key = key

    def dump(self, obj):
        return dump(
            obj,
            self.__file,
            self.__protocol,
            fix_imports=self.__fix_imports,
            key=self.__key,
        )


class Unpickler(pickle.Unpickler):
    def __init__(
        self, file, *, fix_imports=True, encoding="ASCII", errors="strict", key
    ):
        super().__init__(
            file, fix_imports=fix_imports, encoding=encoding, errors=errors
        )
        self.__file = file
        self.__fix_imports = fix_imports
        self.__encoding = encoding
        self.__errors = errors
        self.__key = key

    def load(self):
        return load(
            self.__file,
            fix_imports=self.__fix_imports,
            encoding=self.__encoding,
            errors=self.__errors,
            key=self.__key,
        )
