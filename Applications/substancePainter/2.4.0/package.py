# -*- coding: utf-8 -*-
name = 'substancePainter'
version = '2.4.0'
author = ['substancePainter']
variants = []

def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]
    env.PATH.append(os.path.join(applications_path, "substancePainter", "%s"%version).replace("/", os.sep))

    env.foundry_LICENSE.set("5053@rlm.cashmere.com")

