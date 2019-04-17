# -*- coding: utf-8 -*-
name = 'swig'
version = '3.0.12'
author = ['swig']

requires = ["git",
            "dotnetsdk",
            "cmake",
            "llvm",
            "python",
            "vs"]
variants = []

def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    swig_path = os.path.join(develop_path, "swig", "%s" % version).replace('/', os.sep)
    env.PATH.append(swig_path)

