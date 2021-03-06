# -*- coding: utf-8 -*-

name = u'gflags'

version = '2.2.1'

description = \
    """
    gflags library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    gflags_path = os.path.join(cpp_libs_path, "gflags", "%s"%version)
    gflags_path = gflags_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(gflags_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(gflags_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(gflags_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(gflags_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(gflags_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(gflags_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(gflags_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(gflags_path, 'tbb', "vc14").replace("/", os.sep))

