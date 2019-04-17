# -*- coding: utf-8 -*-
name = 'go'
version = '1.10.3'
author = ['go']

requires = []
variants = []




def commands():
    import os
    develop_path = os.environ["APPLICATIONS_PATH"]
    go_path = os.path.join(develop_path, "go", "%s" % version).replace('/', os.sep)

    env.GOROOT = go_path
    env.GOBIN = os.path.join(go_path, "bin").replace('/', os.sep)

    env.PATH.append(os.path.join(go_path, "bin").replace('/', os.sep))



