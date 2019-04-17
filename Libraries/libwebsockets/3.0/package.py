# -*- coding: utf-8 -*-

name = u'libwebsockets'

version = '3.0'

description = \
    """
    libwebsockets library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libwebsockets_path = os.path.join(cpp_libs_path, "libwebsockets", "%s"%version)
    libwebsockets_path = libwebsockets_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libwebsockets_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libwebsockets_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libwebsockets_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libwebsockets_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libwebsockets_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libwebsockets_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libwebsockets_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libwebsockets_path, 'tbb', "vc14").replace("/", os.sep))

