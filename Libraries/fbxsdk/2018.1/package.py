# -*- coding: utf-8 -*-

name = u'fbxsdk'

version = '2018.1'

description = \
    """
    fbxsdk library 
    """

requires = [ ]

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    fbxsdk_path = os.path.join(cpp_libs_path, "fbxsdk", "%s"%version)
    fbxsdk_path = fbxsdk_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(fbxsdk_path, 'bin').replace("/", os.sep))
        env.INCLUDE.append(os.path.join(fbxsdk_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(fbxsdk_path, 'lib').replace("/", os.sep))

    env.PYTHONPATH.append(os.path.join(fbxsdk_path, 'python', 'lib').replace("/", os.sep))

