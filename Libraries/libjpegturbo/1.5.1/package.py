# -*- coding: utf-8 -*-

name = u'libjpegturbo'

version = '1.5.1'

description = \
    """
    libjpegturbo library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libjpegturbo_path = os.path.join(cpp_libs_path, "libjpegturbo", "%s"%version)
    libjpegturbo_path = libjpegturbo_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libjpegturbo_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libjpegturbo_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libjpegturbo_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libjpegturbo_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libjpegturbo_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libjpegturbo_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libjpegturbo_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libjpegturbo_path, 'tbb', "vc14").replace("/", os.sep))

