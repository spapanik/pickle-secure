from pickle_secure import _utils


def dumps(obj, key, protocol=None, fix_imports=True):
    return _utils.encrypt(obj, key, protocol, fix_imports)


def dump(obj, file, key, protocol=None, fix_imports=True):
    encrypted_data = dumps(obj, key, protocol, fix_imports)
    file.write(encrypted_data)


def loads(obj, key, fix_imports=True, encoding='ASCII', errors='strict'):
    return _utils.decrypt(obj, key, fix_imports, encoding, errors)


def load(file, key, fix_imports=True, encoding='ASCII', errors='strict'):
    encrypted_data = file.read()
    return loads(encrypted_data, key, fix_imports, encoding, errors)
