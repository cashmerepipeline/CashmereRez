# -*- coding: utf-8 -*-

name = u'mpi'

version = '2018.2'

description = \
    """
    intel mpi library 
    """

requires = ["libomp-2018.2"]

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    mkl_path = os.path.join(cpp_libs_path, "mpi", "%s"%version)
    mkl_path = mkl_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(mkl_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(mkl_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(mkl_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(mkl_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkl_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkl_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkl_path, 'mpi').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkl_path, 'tbb', "vc14").replace("/", os.sep))

