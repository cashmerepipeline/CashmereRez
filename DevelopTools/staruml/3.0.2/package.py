# -*- coding: utf-8 -*-
name = 'staruml'
version = '3.0.12'
author = ['staruml']

requires = ["git",
            "vs"]
variants = []

def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    staruml_path = os.path.join(develop_path, "staruml", "%s" % version).replace('/', os.sep)
    env.PATH.append(staruml_path)

