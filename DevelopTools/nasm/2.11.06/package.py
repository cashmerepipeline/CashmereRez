# -*- coding: utf-8 -*-
name = 'nasm'
version = '2.11.06'
author = ['nasm']

requires = []
variants = []

def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]

    nasm_path = os.path.join(develop_path, "nasm", "%s" % version).replace('/', os.sep)

    env.PATH.append(os.path.join(nasm_path).replace('/', os.sep))
    env.PATH.append(os.path.join(nasm_path, "rdoff").replace('/', os.sep))

