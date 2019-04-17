# -*- coding: utf-8 -*-

name = u'intelruntime'

version = '2018.0.2'

description = \
    """
    intel runtime library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    runtime_path = os.path.join(cpp_libs_path, "intelruntime")
    runtime_path = runtime_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(runtime_path, 'compiler').replace("/", os.sep))
        # env.PATH.append(os.path.join(runtime_path, 'daal').replace("/", os.sep))
        # env.PATH.append(os.path.join(runtime_path, 'ipp').replace("/", os.sep))
        # env.PATH.append(os.path.join(runtime_path, 'mkl').replace("/", os.sep))
        # env.PATH.append(os.path.join(runtime_path, 'tbb', "vc14").replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(runtime_path, 'compiler').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(runtime_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(runtime_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(runtime_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(runtime_path, 'tbb', "vc14").replace("/", os.sep))

