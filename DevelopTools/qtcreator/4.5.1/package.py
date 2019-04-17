# -*- coding: utf-8 -*-
name = 'qtcreator'
version = '4.5.1'
author = ['qt']

requires = []
variants = []



def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    qtcreator_path = os.path.join(develop_path, "qtcreator", "%s" % version).replace('/', os.sep)
    env.PATH.append(os.path.join(qtcreator_path, "bin").replace('/', os.sep))
   
