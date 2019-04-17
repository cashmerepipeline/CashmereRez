# -*- coding: utf-8 -*-

name = u'pybind'

version = '2.2.3'

description = \
    """
     library 
    """

requires = [ ]

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    pybind_path = os.path.join(cpp_libs_path, "pybind", "%s"%version)
    pybind_path = pybind_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(pybind_path, 'bin').replace("/", os.sep))
        env.PATH.append(os.path.join(pybind_path, 'lib', "engines").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(pybind_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(pybind_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.PATH.append(os.path.join(pybind_path, 'bin').replace("/", os.sep))
        env.LD_LIBRARY_PATH.append(os.path.join(pybind_path, 'bin').replace("/", os.sep))
        env.LD_LIBRARY_PATH.append(os.path.join(pybind_path, 'lib', "engines").replace("/", os.sep))

