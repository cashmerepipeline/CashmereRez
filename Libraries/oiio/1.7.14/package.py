# -*- coding: utf-8 -*-

name = u'oiio'

version = '1.7.14'

description = \
    """
    oiio library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    oiio_path = os.path.join(cpp_libs_path, "oiio", "%s"%version)
    oiio_path = oiio_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(oiio_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(oiio_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(oiio_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(oiio_path, 'bin').replace("/", os.sep))


