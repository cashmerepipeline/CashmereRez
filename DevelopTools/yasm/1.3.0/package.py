# -*- coding: utf-8 -*-
name = 'yasm'
version = '1.3.0'
author = ['yasm']

requires = []
variants = [            ]

def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]

    yasm_path = os.path.join(develop_path, "yasm", "%s" % version).replace('/', os.sep)

    env.PATH.append(os.path.join(yasm_path).replace('/', os.sep))
    env.PATH.append(os.path.join(yasm_path, "rdoff").replace('/', os.sep))

