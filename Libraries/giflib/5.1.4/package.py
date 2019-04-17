# -*- coding: utf-8 -*-

name = u'giflib'

version = '5.1.4'

description = \
    """
    giflib library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    giflib_path = os.path.join(cpp_libs_path, "giflib", "%s"%version)
    giflib_path = giflib_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(giflib_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(giflib_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(giflib_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(giflib_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(giflib_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(giflib_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(giflib_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(giflib_path, 'tbb', "vc14").replace("/", os.sep))

