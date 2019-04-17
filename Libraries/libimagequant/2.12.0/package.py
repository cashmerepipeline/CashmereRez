# -*- coding: utf-8 -*-

name = u'libimagequant'

version = '2.12.0'

description = \
    """
    libimagequant library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libimagequant_path = os.path.join(cpp_libs_path, "libimagequant", "%s"%version)
    libimagequant_path = libimagequant_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libimagequant_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libimagequant_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libimagequant_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libimagequant_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libimagequant_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libimagequant_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libimagequant_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libimagequant_path, 'tbb', "vc14").replace("/", os.sep))

