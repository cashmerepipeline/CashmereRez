# -*- coding: utf-8 -*-

name = u'mkldnn'

version = '0.15'

description = \
    """
    intel mkldnn library 
    """

requires = ["mkl"]

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    mkldnn_path = os.path.join(cpp_libs_path, "mkldnn", "%s"%version)
    mkldnn_path = mkldnn_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(mkldnn_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(mkldnn_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(mkldnn_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(mkldnn_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkldnn_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkldnn_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkldnn_path, 'mkldnn').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkldnn_path, 'tbb', "vc14").replace("/", os.sep))

