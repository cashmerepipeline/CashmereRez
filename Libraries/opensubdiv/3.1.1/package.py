# -*- coding: utf-8 -*-

name = u'opensubdiv'

version = '1.7.14'

description = \
    """
    opensubdiv library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    opensubdiv_path = os.path.join(cpp_libs_path, "opensubdiv", "%s"%version)
    opensubdiv_path = opensubdiv_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(opensubdiv_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(opensubdiv_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(opensubdiv_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(opensubdiv_path, 'bin').replace("/", os.sep))


