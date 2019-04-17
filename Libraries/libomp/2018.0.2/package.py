# -*- coding: utf-8 -*-

name = u'libomp'

version = '2018.0.2'

description = \
    """
    libomp library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libomp_path = os.path.join(cpp_libs_path, "libomp", "%s"%version)
    libomp_path = libomp_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libomp_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libomp_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libomp_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libomp_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libomp_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libomp_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libomp_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libomp_path, 'tbb', "vc14").replace("/", os.sep))

