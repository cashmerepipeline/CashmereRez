# -*- coding: utf-8 -*-

name = 'uetest'

version = '1.0.0'

description = 'uetest project config'

authors = ['YanGang']

tools = []

requires = [
    'ue-4.22.0'
]

def commands():
    """ """
    import os
    
    env.PROJECT_ROOT.set(r"E:\uetest")
    env.PROJECT_ASSETS_ROOT.set(r"E:\uetest\assets")
    env.PROJECT_SEQUENCE_ROOT.set(r"E:\uetest\sequences")
    
    env.PROJECT_ENVIRONMENT_ROOT.set("")
    
    env.CURRENT_TASK.set("")




