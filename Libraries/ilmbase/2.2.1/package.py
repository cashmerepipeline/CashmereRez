# -*- coding: utf-8 -*-

name = u'ilmbase'

version = '2.2.1'

description = \
    """
    ilmbase library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    ilmbase_path = os.path.join(cpp_libs_path, "ilmbase", "%s"%version)
    ilmbase_path = ilmbase_path.replace("/", os.sep)

    env.ILMBASE_PACKAGE_PREFIX = ilmbase_path

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(ilmbase_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(ilmbase_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(ilmbase_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(ilmbase_path, 'bin').replace("/", os.sep))


