# -*- coding: utf-8 -*-
name = 'kdiff3'
version = '0.9.97'
author = ['git']
variants = []

requires = []



def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    env.PATH.prepend(os.path.join(develop_path, "kdiff3", "%s" % version).replace("/", os.sep))
    env.PATH.prepend(os.path.join(develop_path, "kdiff3", "%s" % version, "bin").replace("/", os.sep))

