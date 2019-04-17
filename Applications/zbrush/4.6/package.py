# -*- coding: utf-8 -*-
name = 'zbrush'
version = '4.6'
author = ['zbrush']

requires = []
variants = []

def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]
    env.PATH.append(os.path.join(applications_path, "zbrush", "%s"%version).replace("/", os.sep))

