# -*- coding: utf-8 -*-
name = '3dcoat'
version = '4.7.24'
author = ['3dcoat']
variants = []

def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]
    env.PATH.prepend(os.path.join(applications_path, "3dcoat", "%s" % version).replace("/", os.sep))

