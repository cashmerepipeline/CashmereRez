# -*- coding: utf-8 -*-

name = u'libtiff'

version = '4.0.9'

description = \
    """
    libtiff library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libtiff_path = os.path.join(cpp_libs_path, "libtiff", "%s"%version)
    libtiff_path = libtiff_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libtiff_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libtiff_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libtiff_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libtiff_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libtiff_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libtiff_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libtiff_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libtiff_path, 'tbb', "vc14").replace("/", os.sep))

