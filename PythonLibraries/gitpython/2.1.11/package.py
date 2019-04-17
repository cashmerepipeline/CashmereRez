# -*- coding: utf-8 -*-

name = u'gitpython'

version = '2.1.11'

description = \
    """
    Simple, fast, extensible JSON encoder/decoder for Python
    """

variants = []

requires = ['git', 'six']

def commands():
    import os

    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "gitpython", "%s" % version)
    env.PYTHONPATH.append(os.path.join(libs_path, "lib").replace("/", os.sep))


