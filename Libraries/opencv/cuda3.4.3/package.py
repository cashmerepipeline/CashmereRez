# -*- coding: utf-8 -*-

name = u'opencv'

version = 'cuda3.4.3'

description = \
    """
    opencv library 
    """

requires = ["numpy"]

variants = []

def commands():
    import os
    import sys
    
    cpp_libs_path = getenv("CPP_LIBS_PATH")

    opencv_path = os.path.join(cpp_libs_path, "opencv", "%s"%version)
    opencv_path = opencv_path.replace("/", os.sep)

    env.OPENCV_DIR = opencv_path
    env.PYTHONPATH.append(os.path.join(opencv_path, 'python').replace("/", os.sep))

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(opencv_path, "bin").replace("/", os.sep))
        env.INCLUDE.append(os.path.join(opencv_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(opencv_path, 'lib').replace("/", os.sep))

    if sys.platform.startswith("linux"):
        env.LD_LIBRARY_PATH.append(os.path.join(opencv_path, 'bin').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(opencv_path, 'daal').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(opencv_path, 'ipp').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(opencv_path, 'mkl').replace("/", os.sep))
        # env.LD_LIBRARY_PATH.append(os.path.join(opencv_path, 'tbb', "vc14").replace("/", os.sep))

