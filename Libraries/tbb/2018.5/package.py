# -*- coding: utf-8 -*-

name = u'tbb'

version = '2018.5'

description = \
    """
    intel tbb library 
    """

requires = ["intelruntime"]

variants = []

def commands():
    import os
    import sys

    vc_version = "vc14"
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    tbb_path = os.path.join(cpp_libs_path, "tbb", "%s"%version)
    tbb_path = tbb_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(tbb_path, "bin", vc_version).replace("/", os.sep))
        env.INCLUDE.append(os.path.join(tbb_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(tbb_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(tbb_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkl_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkl_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkl_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mkl_path, 'tbb', "vc14").replace("/", os.sep))

