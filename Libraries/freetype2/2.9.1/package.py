# -*- coding: utf-8 -*-

name = u'freetype2'

version = '2.9.1'

description = \
    """
    freetype2 library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    freetype2_path = os.path.join(cpp_libs_path, "freetype2", "%s"%version)
    freetype2_path = freetype2_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(freetype2_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(freetype2_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(freetype2_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(freetype2_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(freetype2_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(freetype2_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(freetype2_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(freetype2_path, 'tbb', "vc14").replace("/", os.sep))

