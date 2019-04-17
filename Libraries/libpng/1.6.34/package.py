# -*- coding: utf-8 -*-

name = u'libpng'

version = '1.6.34'

description = \
    """
    libpng library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libpng_path = os.path.join(cpp_libs_path, "libpng", "%s"%version)
    libpng_path = libpng_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libpng_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libpng_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libpng_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libpng_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libpng_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libpng_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libpng_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libpng_path, 'tbb', "vc14").replace("/", os.sep))

