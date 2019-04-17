# -*- coding: utf-8 -*-
name = 'ue4'
version = '4.20.3'
author = ['ue4']

requires = ["python-2.7.11"]
variants = []


def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]
    python_path = os.path.join(applications_path, "python", "2.7.11").replace("/", os.sep)
    
    ue4_path = os.path.join(applications_path, "ue4", "%s"%version).replace("/", os.sep)
    
    env.UE_PYTHON_DIR.set(python_path)
    
    env.PATH.append(os.path.join(ue4_path, "Engine", "Binaries", "Win64").replace("/", os.sep))

