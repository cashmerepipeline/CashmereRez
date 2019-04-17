# -*- coding: utf-8 -*-
name = 'GitExtensions'
version = '2.51.01'
author = ['GitExtensions']
variants = []

requires = ['git',
            'kdiff3']




def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    getex_path = os.path.join(develop_path, "gitextensions", "%s" % version).replace("/", os.sep)

    env.PATH.prepend(getex_path)



