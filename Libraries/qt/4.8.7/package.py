# -*- coding: utf-8 -*-

name = u'qt'

version = '4.8.7'

description = \
    """
    qt library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    qt_path = os.path.join(cpp_libs_path, "qt", "%s"%version)
    qt_path = qt_path.replace("/", os.sep)

    env.QTDIR = qt_path

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(qt_path, 'bin').replace("/", os.sep))
        env.INCLUDE.append(os.path.join(qt_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(qt_path, 'lib').replace("/", os.sep))
        env.QT_PLUGIN_PATH = os.path.join(qt_path, 'plugins').replace("/", os.sep)

    if sys.platform.startswith("linux"):
        env.PATH.append(os.path.join(qt_path, 'bin').replace("/", os.sep))
        env.LD_LIBRARY_PATH.append(os.path.join(qt_path, 'bin').replace("/", os.sep))
        env.QT_PLUGIN_PATH = os.path.join(qt_path, 'plugins').replace("/", os.sep)


