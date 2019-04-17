# -*- coding: utf-8 -*-
name = 'ninja'
version = '1.8.2'
author = ['ninja']
variants = []

requires = []



def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    env.PATH.prepend(os.path.join(develop_path, "ninja", "%s" % version).replace("/", os.sep))

