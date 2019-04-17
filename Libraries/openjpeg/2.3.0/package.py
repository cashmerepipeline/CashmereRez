# -*- coding: utf-8 -*-

name = u'openjpeg'

version = '2.3.0'

description = \
    """
    openjpeg library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    openjpeg_path = os.path.join(cpp_libs_path, "openjpeg", "%s"%version)
    openjpeg_path = openjpeg_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(openjpeg_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(openjpeg_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(openjpeg_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(openjpeg_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(openjpeg_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(openjpeg_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(openjpeg_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(openjpeg_path, 'tbb', "vc14").replace("/", os.sep))

