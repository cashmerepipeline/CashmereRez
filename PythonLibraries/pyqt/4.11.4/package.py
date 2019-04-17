# -*- coding: utf-8 -*-

name = 'pyqt'

version = '4.11.4'

tools = []

variants = []

def commands():
    import os
    
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pyqt", "%s"%version)

    pyqt_path = os.path.join(libs_path, "lib")
    env.PYTHONPATH.append(pyqt_path)

    env.PATH.append(os.path.join(pyqt_path, 'Scripts')).replace('/', os.sep)
    env.PATH.append(os.path.join(pyqt_path, 'PyQt4')).replace('/', os.sep)

def post_commands():
    # these are the builtin modules for this python executable. If we don't
    # include these, some python behavior can be incorrect.
    # import os, os.path
    #
    # libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pyqt")
    pass


    #  path = os.path.join(this.root, "python")
    #  for dirname in os.listdir(path):
        #  path_ = os.path.join(path, dirname)
        #  env.PYTHONPATH.append(path_)

