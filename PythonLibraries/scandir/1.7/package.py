# -*- coding: utf-8 -*-

name = u'scandir'

version = '1.7'

description = \
    """
    scandir tools
    """

variants = []

def commands():
    import os

    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "scandir", "%s" % version)
    env.PYTHONPATH.append(os.path.join(libs_path, "lib").replace("/", os.sep))


