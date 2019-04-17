# -*- coding: utf-8 -*-

name = u'lcms'

version = '2.9.0'

description = \
    """
    lcms library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    lcms_path = os.path.join(cpp_libs_path, "lcms", "%s"%version)
    lcms_path = lcms_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(lcms_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(lcms_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(lcms_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(lcms_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(lcms_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(lcms_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(lcms_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(lcms_path, 'tbb', "vc14").replace("/", os.sep))

