# -*- coding: utf-8 -*-

name = u'hdf5'

version = '1.10.0'

description = \
    """
    hdf5 library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    hdf5_path = os.path.join(cpp_libs_path, "hdf5", "%s"%version)
    hdf5_path = hdf5_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(hdf5_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(hdf5_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(hdf5_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(hdf5_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(hdf5_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(hdf5_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(hdf5_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(hdf5_path, 'tbb', "vc14").replace("/", os.sep))

