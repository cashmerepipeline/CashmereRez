# -*- coding: utf-8 -*-

name = u'libwebp'

version = '1.0.0'

description = \
    """
    libwebp library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libwebp_path = os.path.join(cpp_libs_path, "libwebp", "%s"%version)
    libwebp_path = libwebp_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libwebp_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libwebp_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libwebp_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libwebp_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libwebp_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libwebp_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libwebp_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libwebp_path, 'tbb', "vc14").replace("/", os.sep))

