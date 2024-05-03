# Usage

`pickle_secure` implements a secure way to _pickle_ and _unpickle_ a
python object. It offers the same interface as a pickle, but a key is
also required, which encrypts and decrypts the pickle.

Everything is placed in the `pickle_secure` module.

Three constants are provided:

There are also three exceptions provided, all of them are just the same
as the ones in the original pickle

> The same as the original PickleError from the _pickle_ module

> The same as the original PicklingError from the _pickle_ module

> The same as the original UnpicklingError from the _pickle_ module

Also, the dumping and loading functions present in the original module
are present:

> Dump the object to a bytes object.
>
> param obj
>
> : The object to be pickled
>
> param int protocol
>
> : The pickle protocol to be used, or None to use the default
> protocol
>
> param bool fix_imports
>
> : If the protocol is \< 2, it will try to fix the imports to be
> readable by python2
>
> param str key
>
> : The encryption key
>
> return
>
> : the encrypted pickle of the object
>
> rtype
>
> : bytes

> Dump the obj in the file object named `file`.
>
> param obj
>
> : The object to be pickled
>
> param file
>
> : The file to use to write the pickle
>
> param int protocol
>
> : The pickle protocol to be used, or None to use the default
> protocol
>
> param bool fix_imports
>
> : If the protocol is \< 2, it will try to fix the imports to be
> readable by python2
>
> param str key
>
> : The encryption key

> Retrieve the original object from a bytes object
>
> param bytes bytes_obj
>
> : The encrypted bytes object to be unpickled
>
> param bool fix_imports
>
> : If the protocol is \< 2, it will try to fix the imports to be
> readable by python2
>
> param str encoding
>
> : It is present for compatibility reasons with python2
>
> param str errors
>
> : It is present for compatibility reasons with python2
>
> param str key
>
> : The encryption key
>
> return
>
> : The object that was originally pickled

> Retrieve the original object from a file
>
> param file
>
> : The file containing the encrypted pickle
>
> param bool fix_imports
>
> : If the protocol is \< 2, it will try to fix the imports to be
> readable by python2
>
> param str encoding
>
> : It is present for compatibility reasons with python2
>
> param str errors
>
> : It is present for compatibility reasons with python2
>
> param str key
>
> : The encryption key
>
> return
>
> : The object that was originally pickled
