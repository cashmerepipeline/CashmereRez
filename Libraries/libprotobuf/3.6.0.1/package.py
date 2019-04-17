# -*- coding: utf-8 -*-

name = u'libprotobuf'

version = '3.6.0.1'

description = \
    """
    libprotobuf library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libprotobuf_path = os.path.join(cpp_libs_path, "libprotobuf", "%s"%version)
    libprotobuf_path = libprotobuf_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libprotobuf_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libprotobuf_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libprotobuf_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libprotobuf_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libprotobuf_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libprotobuf_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libprotobuf_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libprotobuf_path, 'tbb', "vc14").replace("/", os.sep))

