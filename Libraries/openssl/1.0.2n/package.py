# -*- coding: utf-8 -*-

name = u'openssl'

version = '1.0.2n'

description = \
    """
     library 
    """

requires = [ ]

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    openssl_path = os.path.join(cpp_libs_path, "openssl", "%s"%version)
    openssl_path = openssl_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(openssl_path, 'bin').replace("/", os.sep))
        env.PATH.append(os.path.join(openssl_path, 'lib', "engines").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(openssl_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(openssl_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.PATH.append(os.path.join(openssl_path, 'bin').replace("/", os.sep))
        env.LD_LIBRARY_PATH.append(os.path.join(openssl_path, 'bin').replace("/", os.sep))
        env.LD_LIBRARY_PATH.append(os.path.join(openssl_path, 'lib', "engines").replace("/", os.sep))

