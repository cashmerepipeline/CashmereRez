# -*- coding: utf-8 -*-

name = u'icu'

version = '60.2'

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

    icu_path = os.path.join(cpp_libs_path, "icu", "%s"%version)
    icu_path = icu_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(icu_path, 'bin').replace("/", os.sep))
        env.INCLUDE.append(os.path.join(icu_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(icu_path, 'lib').replace("/", os.sep))

