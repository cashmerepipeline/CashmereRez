# -*- coding: utf-8 -*-
name = 'realflow'
version = '2015'
author = ['realflow']

requires = []
variants = []

def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]
    env.PATH.append(os.path.join(applications_path, "realflow", "%s"%version).replace("/", os.sep))

