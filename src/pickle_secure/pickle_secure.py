import pickle

from pickle_secure import utils

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
    pass


class Unpickler(pickle.Unpickler):
    pass
