# -*- coding: utf-8 -*-

name = u'cub'

version = '3.3.4'

description = \
    """
    cub library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    eigen_path = os.path.join(cpp_libs_path, "cub", "%s"%version)
    eigen_path = eigen_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        # env.PATH.append(os.path.join(eigen_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(eigen_path, 'include').replace("/", os.sep))
        # env.LIB.append(os.path.join(eigen_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(eigen_path, 'bin').replace("/", os.sep))


