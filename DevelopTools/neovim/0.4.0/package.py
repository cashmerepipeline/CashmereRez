# -*- coding: utf-8 -*-
name = 'neovim'
version = '0.4.0'
author = ['neovim']
variants = []

def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    neovim_path = os.path.join(develop_path, "neovim", "%s" % version).replace('/', os.sep)

    env.PATH.prepend(os.path.join(neovim_path, "bin").replace("/", os.sep))

