# -*- coding: utf-8 -*-
name = 'bazel'
version = '0.17.2'
author = ['bazel']
variants = []
requires = ["git",
            "gnuwin32",
            "java",
            "msys2"]


def commands():
    import os

    develop_path = os.environ["DEVELOP_TOOLS_PATH"]
    bazel_path = os.path.join(develop_path, "bazel", "%s" % version).replace("/", os.sep)
    env.PATH.append(bazel_path)

    env.BAZEL_SH="D:/CashmereRuntime/Applications/msys2/1.0.0/usr/bin/bash.exe"



