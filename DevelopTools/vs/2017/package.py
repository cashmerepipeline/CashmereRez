# -*- coding: utf-8 -*-
name = 'vs'
version = '2017'
author = ['microsoft']
variants = []



def commands():
    import os

    winkit_path = r"C:\Program Files (x86)\Windows Kits\10\bin\10.0.17134.0\x64"
    vs_path = r"C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE"
    vc_path = r"C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC"
    vcvars_path = r"C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build"

    env.PATH.prepend(vs_path)
    env.PATH.prepend(vcvars_path)
    env.PATH.prepend(winkit_path)



