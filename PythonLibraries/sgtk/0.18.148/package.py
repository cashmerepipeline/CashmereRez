# -*- coding: utf-8 -*-

name = 'sgtk'

version = '0.18.148'

tools = []

variants = []



def commands():
    # these are the builtin modules for this python executable. If we don't
    # include these, some python behavior can be incorrect.
    import os, os.path
    
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "sgtk", "%s"%version)

    env.PYTHONPATH.append(os.path.join(libs_path, "lib").replace("/", os.sep))


