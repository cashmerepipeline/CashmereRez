# -*- coding: utf-8 -*-
name = '3dsmax'
version = '2016'
author = ['3dsmax']

requires = []
variants = []

def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]
    env.PATH.prepend(os.path.join(applications_path, "3dsmax", "%s"%version).replace("/", os.sep))

