# -*- coding: utf-8 -*-

name = u'qtpy'

version = '1.4.2'

description = \
    """
    qt.py
    """

requires = []

variants = []



def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "qtpy", "%s" % version)

    env.PYTHONPATH.append(os.path.join(libs_path, 'lib'))
