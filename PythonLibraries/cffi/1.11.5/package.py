# -*- coding: utf-8 -*-

name = u'cffi'

version = '1.11.5'

description = \
    """
    cffi libraries
    """

requires = ["pycparser",
            "pytest"]

variants = []

def commands():
    import os

    cffi_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "cffi", "%s"%version)

    # env.PATH.append(os.path.join(cffi_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(cffi_libs_path, 'lib'))
