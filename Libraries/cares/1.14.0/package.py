# -*- coding: utf-8 -*-

name = u'cares'

version = '1.14.0'

description = \
    """
    cares library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    cares_path = os.path.join(cpp_libs_path, "cares", "%s"%version)
    cares_path = cares_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(cares_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(cares_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(cares_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(cares_path, 'bin').replace("/", os.sep))


