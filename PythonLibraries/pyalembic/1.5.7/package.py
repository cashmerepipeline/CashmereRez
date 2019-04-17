# -*- coding: utf-8 -*-

name = u'pyalembic'

version = '1.5.7'

description = \
    """
    alembic python binding
    """

requires = ['python-2.7', 'pyqt-4', 'pyopengl', 'numpy']

variants = []

def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pyalembic", "%s"%version)

    env.PATH.append(libs_path)
    env.PATH.append(os.path.join(libs_path, 'lib').replace("/", os.sep))
    env.PATH.append(os.path.join(libs_path, 'Scripts').replace("/", os.sep))

    env.PYTHONPATH.append(os.path.join(libs_path, 'lib'.replace("/", os.sep)))

    env.ABCVIEW_PATH.set(os.path.join(libs_path, 'Scripts').replace("/", os.sep))
