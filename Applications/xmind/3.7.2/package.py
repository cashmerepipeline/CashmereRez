# -*- coding: utf-8 -*-
name = 'xmind'
version = '3.7.2'
author = ['xmind']

requires = ["java"]
variants = []


def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]
    
    xmind_path = os.path.join(applications_path, "xmind", "%s"%version).replace("/", os.sep)
    
    env.PATH.append(os.path.join(xmind_path))

