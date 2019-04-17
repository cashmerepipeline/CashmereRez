# -*- coding: utf-8 -*-
name = 'clarisse'
version = '3.0.8'
author = ['clarisse']
variants = []

def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]
    
    env.PATH.prepend(os.path.join(applications_path, "clarisse", "%s"%version).replace("/", os.sep))


