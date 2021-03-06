# -*- coding: utf-8 -*-

name = u'libevent'

version = '2.1.8'

description = \
    """
    libevent library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libevent_path = os.path.join(cpp_libs_path, "libevent", "%s"%version)
    libevent_path = libevent_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libevent_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libevent_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libevent_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libevent_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libevent_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libevent_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libevent_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libevent_path, 'tbb', "vc14").replace("/", os.sep))

