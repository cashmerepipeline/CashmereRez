# -*- coding: utf-8 -*-

name = u'libjpeg'

version = '1.2.8'

description = \
    """
    libjpeg library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libjpeg_path = os.path.join(cpp_libs_path, "libjpeg", "%s"%version)
    libjpeg_path = libjpeg_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libjpeg_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libjpeg_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libjpeg_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libjpeg_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libjpeg_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libjpeg_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libjpeg_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libjpeg_path, 'tbb', "vc14").replace("/", os.sep))

