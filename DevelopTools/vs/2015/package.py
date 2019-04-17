# -*- coding: utf-8 -*-
name = 'vs'
version = '2015'
author = ['microsoft']
variants = []



def commands():
    import os

    winkit_path = r"C:\Program Files (x86)\Windows Kits\10\bin\10.0.17134.0\x64"
    vs_path = r"C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE"
    vc_path = r"C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC"

    env.PATH.prepend(vs_path)
    env.PATH.prepend(vc_path)
    env.PATH.prepend(winkit_path)



