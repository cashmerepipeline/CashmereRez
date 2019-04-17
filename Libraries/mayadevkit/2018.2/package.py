# -*- coding: utf-8 -*-

name = u'mayadevkit'

version = '2018.2'

description = \
    """
    mayadevkit library 
    """

requires = ["qt-asdk"]

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    mayadevkit_path = os.path.join(cpp_libs_path, "mayadevkit", "%s"%version)
    mayadevkit_path = mayadevkit_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(mayadevkit_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(mayadevkit_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(mayadevkit_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(mayadevkit_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mayadevkit_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mayadevkit_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mayadevkit_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(mayadevkit_path, 'tbb', "vc14").replace("/", os.sep))

