import pickle

from pickle_secure import utils

API_VERSION = "3.6"
HIGHEST_PROTOCOL = pickle.HIGHEST_PROTOCOL
DEFAULT_PROTOCOL = pickle.DEFAULT_PROTOCOL
PickleError = pickle.PickleError
PicklingError = pickle.PicklingError
UnpicklingError = pickle.UnpicklingError


def dumps(obj, key, protocol=None, *, fix_imports=True):
    return utils.encrypt(obj, key, protocol, fix_imports)


def dump(obj, file, key, protocol=None, *, fix_imports=True):
    file.write(dumps(obj, key=key, protocol=protocol, fix_imports=fix_imports))


def loads(bytes_object, key, *, fix_imports=True, encoding="ASCII", errors="strict"):
    return utils.decrypt(bytes_object, key, fix_imports, encoding, errors)


def load(file, key, *, fix_imports=True, encoding="ASCII", errors="strict"):
    return loads(
        file.read(), key, fix_imports=fix_imports, encoding=encoding, errors=errors,
    )


class Pickler(pickle.Pickler):
    def __init__(self, file, key, protocol=None, *, fix_imports=True):
        super().__init__(file, protocol, fix_imports=fix_imports)
        self.__file = file
        self.__key = key
        self.__protocol = protocol
        self.__fix_imports = fix_imports

    def dump(self, obj):
        return dump(
            obj,
            self.__file,
            self.__key,
            self.__protocol,
            fix_imports=self.__fix_imports,
        )


class Unpickler(pickle.Unpickler):
    def __init__(
        self, file, key, *, fix_imports=True, encoding="ASCII", errors="strict"
    ):
        super().__init__(
            file, fix_imports=fix_imports, encoding=encoding, errors=errors
        )
        self.__file = file
        self.__key = key
        self.__fix_imports = fix_imports
        self.__encoding = encoding
        self.__errors = errors

    def load(self):
        return load(
            self.__file,
            self.__key,
            fix_imports=self.__fix_imports,
            encoding=self.__encoding,
            errors=self.__errors,
        )
