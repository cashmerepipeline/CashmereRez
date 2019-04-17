# -*- coding: utf-8 -*-
name = 'gnuwin32'
version = '1.0.0'
author = ['gnuwin32']

requires = []
variants = []



def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    gnuwin32_path = os.path.join(develop_path, "gnuwin32", "%s" % version).replace('/', os.sep)

    env.PATH.append(os.path.join(gnuwin32_path, "bin").replace('/', os.sep))
       

