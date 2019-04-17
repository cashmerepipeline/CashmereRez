# -*- coding: utf-8 -*-

name = u'websocketpp'

version = '1.2.8'

description = \
    """
    websocketpp library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    websocketpp_path = os.path.join(cpp_libs_path, "websocketpp", "%s"%version)
    websocketpp_path = websocketpp_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(websocketpp_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(websocketpp_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(websocketpp_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(websocketpp_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(websocketpp_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(websocketpp_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(websocketpp_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(websocketpp_path, 'tbb', "vc14").replace("/", os.sep))

