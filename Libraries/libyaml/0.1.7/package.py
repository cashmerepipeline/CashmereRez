# -*- coding: utf-8 -*-

name = u'libyaml'

version = '0.1.7'

description = \
    """
    libyaml library 
    """

requires = []

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    libyaml_path = os.path.join(cpp_libs_path, "libyaml", "%s"%version)
    libyaml_path = libyaml_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(libyaml_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(libyaml_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(libyaml_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(libyaml_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libyaml_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libyaml_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libyaml_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(libyaml_path, 'tbb', "vc14").replace("/", os.sep))

