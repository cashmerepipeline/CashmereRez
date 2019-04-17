# -*- coding: utf-8 -*-

name = u'libzmq'

version = '4.2.5'

description = \
    """
    libzmq library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libzmq_path = os.path.join(cpp_libs_path, "libzmq", "%s"%version)
    libzmq_path = libzmq_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libzmq_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libzmq_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libzmq_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libzmq_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libzmq_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libzmq_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libzmq_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libzmq_path, 'tbb', "vc14").replace("/", os.sep))

