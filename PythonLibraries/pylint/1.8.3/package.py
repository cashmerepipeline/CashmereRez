# -*- coding: utf-8 -*-

name = u"pylint"

version = "1.8.3"

description = \
    """
    pylint libraries
    """

requires = ["colorama", "singledispatch", "six", "astroid", "isort"]

variants = []

def commands():
    import os

    pylint_libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pylint", "%s"%version).replace("/", os.sep)

    env.PYTHONPATH.append(os.path.join(pylint_libs_path, "lib").replace("/", os.sep))
    env.PATH.append(os.path.join(pylint_libs_path, "Scripts").replace("/", os.sep))
