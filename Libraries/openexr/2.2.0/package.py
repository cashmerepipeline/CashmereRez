# -*- coding: utf-8 -*-

name = u'openexr'

version = '2.2.1'

description = \
    """
    openexr library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    openexr_path = os.path.join(cpp_libs_path, "openexr", "%s"%version)
    openexr_path = openexr_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(openexr_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(openexr_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(openexr_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(openexr_path, 'bin').replace("/", os.sep))


