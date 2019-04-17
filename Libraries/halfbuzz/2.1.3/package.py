# -*- coding: utf-8 -*-

name = u'halfbuzz'

version = '2.1.3'

description = \
    """
    halfbuzz library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    halfbuzz_path = os.path.join(cpp_libs_path, "halfbuzz", "%s"%version)
    halfbuzz_path = halfbuzz_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(halfbuzz_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(halfbuzz_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(halfbuzz_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(halfbuzz_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(halfbuzz_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(halfbuzz_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(halfbuzz_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(halfbuzz_path, 'tbb', "vc14").replace("/", os.sep))

