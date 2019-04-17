# -*- coding: utf-8 -*-
name = 'flutter'
version = '1.2.1'
author = ['flutter']

requires = []
variants = []




def commands():
    import os
    develop_path = os.environ["APPLICATIONS_PATH"]
    flutter_path = os.path.join(develop_path, "flutter", "%s" % version).replace('/', os.sep)

    env.FLUTTER_ROOT = flutter_path
    env.FLUTTER_ENGINE_VERSION = "3757390fa4b00d2d261bfdf5182d2e87c9113ff9"
    env.FlutterBIN = os.path.join(flutter_path, "bin").replace('/', os.sep)

    env.PATH.append(os.path.join(flutter_path, "bin").replace('/', os.sep))



