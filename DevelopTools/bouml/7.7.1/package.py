# -*- coding: utf-8 -*-
name = 'bouml'
version = '3.0.12'
author = ['bouml']

requires = ["git",
            "vs"]
variants = []

def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    bouml_path = os.path.join(develop_path, "bouml", "%s" % version).replace('/', os.sep)
    env.PATH.append(bouml_path)

