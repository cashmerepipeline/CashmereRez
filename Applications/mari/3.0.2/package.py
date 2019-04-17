# -*- coding: utf-8 -*-
name = 'mari'
version = '3.0.2'
author = ['mari']
variants = []

def commands():
    import os

    env.foundry_LICENSE.set("5053@rlm.cashmere.com")

    applications_path = os.environ["APPLICATIONS_PATH"]

    env.PATH.prepend(os.path.join(applications_path, "mari", "%s"%version, "Bundle", "bin").replace("/", os.sep))

