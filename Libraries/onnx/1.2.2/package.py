# -*- coding: utf-8 -*-

name = u'onnx'

version = '1.2.2'

description = \
    """
    onnx library 
    """

requires = ["protobuf",
            "numpy",
            "typing",
            "pybind"]

variants = []

def commands():
    import os
    import sys

    cpp_libs_path = getenv("CPP_LIBS_PATH")

    onnx_path = os.path.join(cpp_libs_path, "onnx", "%s"%version)
    onnx_path = onnx_path.replace("/", os.sep)

    if sys.platform.startswith("win32"):
        env.PATH.append(os.path.join(onnx_path, 'bin').replace("/", os.sep))
        env.INCLUDE.append(os.path.join(onnx_path, 'include').replace("/", os.sep))
        env.LIB.append(os.path.join(onnx_path, 'lib').replace("/", os.sep))


    env.PYTHONPATH.append(os.path.join(onnx_path, 'python', 'lib').replace("/", os.sep))
    env.PATH.append(os.path.join(onnx_path, 'python', 'Scripts').replace("/", os.sep))