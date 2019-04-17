# -*- coding: utf-8 -*-

name = u'freeglut'

version = '3.0.0'

description = \
    """
    freeglut library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    freeglut_path = os.path.join(cpp_libs_path, "freeglut", "%s"%version)
    freeglut_path = freeglut_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(freeglut_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(freeglut_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(freeglut_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(freeglut_path, 'bin').replace("/", os.sep))


