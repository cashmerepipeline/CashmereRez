# -*- coding: utf-8 -*-

name = u'audioread'

version = '2.1.5'

description = \
    """
    audioread libraries
    """

requires = []

variants = []

def commands():
    import os

    audioread_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "audioread", "%s"%version)

    # env.PATH.append(os.path.join(audioread_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(audioread_libs_path, 'lib'))
