# -*- coding: utf-8 -*-

name = u'freetype'

version = '2.9.1'

description = \
    """
    freetype library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    freetype_path = os.path.join(cpp_libs_path, "freetype", "%s"%version)
    freetype_path = freetype_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(freetype_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(freetype_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(freetype_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(freetype_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(freetype_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(freetype_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(freetype_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(freetype_path, 'tbb', "vc14").replace("/", os.sep))

