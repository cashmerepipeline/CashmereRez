# -*- coding: utf-8 -*-

name = u'google'

version = '2.6.11'

description = \
    """
    google python libraries
    """

requires = []

variants = []

def commands():
    import os

    google_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "google", "%s"%version)

    # env.PATH.append(os.path.join(google_libs_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(google_libs_path, 'lib'))
