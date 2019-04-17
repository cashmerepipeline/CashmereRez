# -*- coding: utf-8 -*-
name = 'mercurial'
version = '4.5.2'
author = ['mercurial']
variants = []

def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    mercurial_path = os.path.join(develop_path, "mercurial", "%s" % version).replace('/', os.sep)

    env.PATH.prepend(mercurial_path)

