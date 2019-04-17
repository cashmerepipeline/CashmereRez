# -*- coding: utf-8 -*-

name = u'qdarkstyle'

version = '2.5.4'

description = \
    """
    qt.py
    """

requires = []

variants = []



def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "qdarkstyle", "%s" % version)

    env.PYTHONPATH.append(os.path.join(libs_path, 'lib'))
