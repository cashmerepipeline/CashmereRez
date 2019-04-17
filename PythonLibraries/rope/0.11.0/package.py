# -*- coding: utf-8 -*-

name = u'rope'

version = '0.11.0'

description = \
    """
    rope tools
    """

variants = []

def commands():
    import os

    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "rope", "%s" % version)
    env.PYTHONPATH.append(os.path.join(libs_path, "lib").replace("/", os.sep))
