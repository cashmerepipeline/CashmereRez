# -*- coding: utf-8 -*-
name = 'vscode'
version = '1.33.0'
author = ['microsoft']

requires = ["git",
            "dotnetsdk",
            "cmake",
            "llvm",
            "pylint",
            "jedi",
            "autopep8",
            "rope"]
variants = []

def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    vscode_path = os.path.join(develop_path, "vscode", "%s" % version).replace('/', os.sep)
    env.PATH.append(os.path.join(vscode_path).replace('/', os.sep))

