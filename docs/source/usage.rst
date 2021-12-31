=====
Usage
=====

``pickle_secure`` implements a secure way to *pickle* and *unpickle*
a python object. It offers the same interface as a pickle, but a key is also required,
which encrypts and decrypts the pickle.


.. py:module:: pickle_secure

Everything is placed in the ``pickle_secure`` module.

Three constants are provided:

.. py:data:: API_VERSION
    :type: str

    The python version of the pickle that pickle_secure targets

.. py:data:: HIGHEST_PROTOCOL
    :type: int

    The same as the original HIGHEST_PROTOCOL from the *pickle* module

.. py:data:: DEFAULT_PROTOCOL
    :type: int

    The same as the original DEFAULT_PROTOCOL from the *pickle* module

There are also three exceptions provided, all of them are just the same as the ones in the original pickle

.. py:exception:: PickleError

    The same as the original PickleError from the *pickle* module


.. py:exception:: PicklingError

    The same as the original PicklingError from the *pickle* module


.. py:exception:: UnpicklingError

    The same as the original UnpicklingError from the *pickle* module


Also, the dumping and loading functions present in the original module are present:

.. py:function:: def dumps(obj, protocol=None, *, fix_imports=True, key):

   Dump the object to a bytes object.

   :param obj: The object to be pickled
   :param int protocol: The pickle protocol to be used, or None to use the default protocol
   :param bool fix_imports: If the protocol is < 2, it will try to fix the imports to be readable by python2
   :param str key: The encryption key
   :return: the encrypted pickle of the object
   :rtype: bytes

.. py:function:: def dump(obj, file, protocol=None, *, fix_imports=True, key):

   Dump the obj in the file object named ``file``.

   :param obj: The object to be pickled
   :param file: The file to use to write the pickle
   :param int protocol: The pickle protocol to be used, or None to use the default protocol
   :param bool fix_imports: If the protocol is < 2, it will try to fix the imports to be readable by python2
   :param str key: The encryption key

.. py:function:: def loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict", key):

   Retrieve the original object from a bytes object

   :param bytes bytes_obj: The encrypted bytes object to be unpickled
   :param bool fix_imports: If the protocol is < 2, it will try to fix the imports to be readable by python2
   :param str encoding: It is present for compatibility reasons with python2
   :param str errors: It is present for compatibility reasons with python2
   :param str key: The encryption key
   :return: The object that was originally pickled

.. py:function:: def load(file, key, *, fix_imports=True, encoding="ASCII", errors="strict"):

   Retrieve the original object from a file

   :param file: The file containing the encrypted pickle
   :param bool fix_imports: If the protocol is < 2, it will try to fix the imports to be readable by python2
   :param str encoding: It is present for compatibility reasons with python2
   :param str errors: It is present for compatibility reasons with python2
   :param str key: The encryption key
   :return: The object that was originally pickled
