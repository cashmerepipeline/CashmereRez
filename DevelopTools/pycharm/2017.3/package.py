# -*- coding: utf-8 -*-
name = 'pycharm'
version = '2017.3'
author = ['pycharm']

requires = ["git"]
variants = []

def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    pycharm_path = os.path.join(develop_path, "pycharm", "%s" % version).replace('/', os.sep)
    env.PATH.append(os.path.join(pycharm_path, "bin").replace('/', os.sep))

