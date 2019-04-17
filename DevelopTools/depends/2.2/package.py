# -*- coding: utf-8 -*-
name = 'depends'
version = '0.15.0'
author = ['depends']
variants = []



def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    depends_path = os.path.join(develop_path, "depends", "%s" % version).replace("/", os.sep)
    env.PATH.append(depends_path)



