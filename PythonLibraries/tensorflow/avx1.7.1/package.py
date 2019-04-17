# -*- coding: utf-8 -*-

name = u'tensorflow'

version = 'avx1.7.1'

description = \
    """
    tensorflow library 
    """

requires = ["cuda",
            "numpy",
            "six",
            "markdown",
            "libprotobuf",
            "scipy",
            "absl",
            "astor",
            "backports",
            "bleach",
            "futures",
            "mock",
            "html5lib",
            "grpcio",
            "pbr",
            "protobuf",
            "werkzeug",
            "termcolor",
            "gast"
            ]

variants = []

def commands():
    import os
    
    tensorflow_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "tensorflow", "%s"%version)

    env.PATH.append(os.path.join(tensorflow_libs_path, 'bin'))

    env.PYTHONPATH.append(os.path.join(tensorflow_libs_path, 'lib'))
