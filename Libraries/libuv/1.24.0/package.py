# -*- coding: utf-8 -*-

name = u'libuv'

version = '1.24.0'

description = \
    """
    libuv library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libuv_path = os.path.join(cpp_libs_path, "libuv", "%s"%version)
    libuv_path = libuv_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libuv_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libuv_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libuv_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libuv_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libuv_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libuv_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libuv_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libuv_path, 'tbb', "vc14").replace("/", os.sep))

