# -*- coding: utf-8 -*-
name = 'notepadpp'
version = '7.5.6'
author = ['notepadpp']
variants = []

requires = []



def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    env.PATH.prepend(os.path.join(develop_path, "notepadpp", "%s" % version).replace("/", os.sep))

