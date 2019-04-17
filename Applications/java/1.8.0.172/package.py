# -*- coding: utf-8 -*-
name = 'java'
version = '1.8.0.172'
author = ['java']

requires = []
variants = []



def commands():
    import os
    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    java_path = os.path.join(develop_path, "java", "%s" % version).replace('/', os.sep)

    env.JAVA_HOME = java_path
    env.PATH.append(os.path.join(java_path, "bin").replace('/', os.sep))
       

