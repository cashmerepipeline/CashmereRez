# -*- coding: utf-8 -*-

name = u'dlib'

version = '3.3.4'

description = \
    """
    dlib library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    dlib_path = os.path.join(cpp_libs_path, "dlib", "%s"%version)
    dlib_path = dlib_path.replace("/", os.sep)

    env.PYTHONPATH.append(os.path.join(dlib_path, 'python').replace("/", os.sep))

    if sys.platform.startswith("win32"):
        # env.PATH.append(os.path.join(dlib_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(dlib_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(dlib_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(dlib_path, 'bin').replace("/", os.sep))


