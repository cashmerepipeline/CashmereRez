# -*- coding: utf-8 -*-
name = 'git'
version = '2.16.2'
author = ['git']
variants = [            ]

def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    env.PATH.prepend(os.path.join(develop_path, "git", "%s" % version).replace("/", os.sep))
    env.PATH.prepend(os.path.join(develop_path, "git", "%s" % version, "cmd").replace("/", os.sep))

