# -*- coding: utf-8 -*-

name = u'resampy'

version = '0.2.0'

description = \
    """
    resampy library 
    """

requires = ["six",
            "numba",
            "scipy"]

variants = []


def commands():
    import os

    resampy_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "resampy", "%s" % version)

    # env.PATH.append(os.path.join(resampy_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(resampy_libs_path, 'lib'))
