# -*- coding: utf-8 -*-

name = u'boost'

version = '1.61.0'

description = \
    """
    boost library 
    """

requires = [ ]

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    boost_path = os.path.join(cpp_libs_path, "boost", "%s"%version)
    boost_path = boost_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(boost_path, 'bin').replace("/", os.sep))
        env.INCLUDE.append(os.path.join(boost_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(boost_path, 'lib').replace("/", os.sep))

