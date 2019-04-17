# -*- coding: utf-8 -*-
name = 'photoshop'
version = '13.0'
author = ['photoshop']

requires = []
variants = []

def commands():
    import os
    # env.PATH.append("C:/Program Files/Adobe/Adobe Photoshop CS6 (64 Bit)")
    applications_path = os.environ["APPLICATIONS_PATH"]

    env.PATH.append(os.path.join(applications_path, "photoshop", "%s"%version).replace("/", os.sep))

