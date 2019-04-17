# -*- coding: utf-8 -*-

name = u're2'

version = '20180701'

description = \
    """
    re2 library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    re2_path = os.path.join(cpp_libs_path, "re2", "%s"%version)
    re2_path = re2_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(re2_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(re2_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(re2_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(re2_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(re2_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(re2_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(re2_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(re2_path, 'tbb', "vc14").replace("/", os.sep))

