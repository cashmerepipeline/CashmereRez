# -*- coding: utf-8 -*-

name = 'nodejs'

version = '10.14.1'

author = ['nodejs']

tools = ["nodejs"]

requires = [] 

variants = [ ]



def commands():
    import os

    applications_path = os.environ["APPLICATIONS_PATH"]

    nodejs_path = os.path.join(applications_path, "nodejs", "%s"%version).replace("/", os.sep)

    env.PATH.append(nodejs_path)
    