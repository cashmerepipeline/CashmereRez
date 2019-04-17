# -*- coding: utf-8 -*-

name = u'googletest'

version = '1.8.3'

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

    googletest_path = os.path.join(cpp_libs_path, "googletest")
    googletest_path = googletest_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.INCLUDE.append(os.path.join(googletest_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(googletest_path, 'lib').replace("/", os.sep))

