# -*- coding: utf-8 -*-

name = u'z3'

version = '4.6.0'

description = \
    """
    z3 library 
    """

requires = []

variants = [['platform-windows'],
            ]

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("DEVELOP_TOOLS_PATH")

    z3_path = os.path.join(cpp_libs_path, "z3", "%s" % version)
    z3_path = z3_path.replace("/", os.sep)


    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(z3_path, "bin").replace("/", os.sep))
        env.PATH.append(os.path.join(z3_path, "lib").replace("/", os.sep))
        
        env.INCLUDE.append(os.path.join(z3_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(z3_path, 'lib').replace("/", os.sep))

        env.PYTHONPATH.append(os.path.join(z3_path, 'python').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(z3_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(z3_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(z3_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(z3_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(z3_path, 'tbb', "vc14").replace("/", os.sep))

