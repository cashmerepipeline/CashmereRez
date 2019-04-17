# -*- coding: utf-8 -*-
name = 'svn'
version = '1.9.7'
author = ['svn']
variants = []

def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    neovim_path = os.path.join(develop_path, "svn", "%s" % version).replace('/', os.sep)

    env.PATH.prepend(os.path.join(neovim_path, "bin").replace("/", os.sep))

