# -*- coding: utf-8 -*-

name = 'pyside'

version = '1.2.4'

tools = []

variants = []


def commands():
    import os

    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pyside", "%s" % version)

    env.PYTHONPATH.append(os.path.join(libs_path, 'lib').replace('/', os.sep))

    env.PATH.append(os.path.join(libs_path, 'Scripts').replace('/', os.sep))
    env.PATH.append(os.path.join(libs_path, 'lib', 'PySide').replace('/', os.sep))
