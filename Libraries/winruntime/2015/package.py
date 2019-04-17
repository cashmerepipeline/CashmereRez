# -*- coding: utf-8 -*-

name = u'winruntime'

version = '0.15'

description = \
    """
    intel winruntime library 
    """

requires = ["mkl"]

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    winruntime_path = os.path.join(cpp_libs_path, "winruntime", "%s"%version)
    winruntime_path = winruntime_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(winruntime_path, "bin").replace("/", os.sep))
        # env.INCLUDE.append(os.path.join(winruntime_path, 'include').replace("/", os.sep))
        # env.LIB.append(os.path.join(winruntime_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(winruntime_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(winruntime_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(winruntime_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(winruntime_path, 'winruntime').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(winruntime_path, 'tbb', "vc14").replace("/", os.sep))

