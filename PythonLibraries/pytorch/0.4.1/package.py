# -*- coding: utf-8 -*-

name = u'pytorch'

version = '0.4.1'

description = \
    """
    pytorch library 
    """

requires = ["pyyaml",
            "typing",
            "cuda",
            "numpy",
            "mkl",
            "cffi",
            "pillow",
            "isort",
            "psutil"]

variants = []

def commands():
    import os

    pytorch_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pytorch", "%s"%version)

    # env.PATH.append(os.path.join(pytorch_libs_path, 'lib', "torch", "lib").replace("/", os.sep) )

    env.PYTHONPATH.append(os.path.join(pytorch_libs_path, 'lib'))
