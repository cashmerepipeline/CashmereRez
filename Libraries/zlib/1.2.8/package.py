# -*- coding: utf-8 -*-

name = u'zlib'

version = '1.2.8'

description = \
    """
    zlib library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    zlib_path = os.path.join(cpp_libs_path, "zlib", "%s"%version)
    zlib_path = zlib_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(zlib_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(zlib_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(zlib_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(zlib_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(zlib_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(zlib_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(zlib_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(zlib_path, 'tbb', "vc14").replace("/", os.sep))

