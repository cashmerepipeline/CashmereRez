# -*- coding: utf-8 -*-

name = u'librosa'

version = '0.6.0'

description = \
    """
    librosa libraries
    """

requires = ["scipy",
            "audioread",
            "numpy",
            "llvmlite",
            "google",
            "resampy",
            "joblib",
            "decorator",
            "sklearn"
            ]

variants = []

def commands():
    import os

    librosa_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "librosa", "%s"%version)

    # env.PATH.append(os.path.join(librosa_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(librosa_libs_path, 'lib'))
    env.PATH.append(os.path.join(librosa_libs_path, 'Scripts'))
