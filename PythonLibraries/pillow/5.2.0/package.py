# -*- coding: utf-8 -*-

name = u'pillow'

version = '5.2.0'

description = \
    """
    pillow
    """

requires = ['libtiff',
            'libpng',
            'libwebp',
            'giflib',
            'freetype',
            'openjpeg',
            'libjpegturbo',
            'libimagequant',
            'zlib',
            'six'
            ]

variants = []




def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "pillow", "%s" % version)

    env.PATH.append(os.path.join(libs_path, 'lib'))
    env.PATH.append(os.path.join(libs_path, 'Scripts'))

    env.PYTHONPATH.append(os.path.join(libs_path, 'lib'))
