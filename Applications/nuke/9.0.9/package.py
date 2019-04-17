# -*- coding: utf-8 -*-

name = 'nuke'

version = '10.5.3'

author = ['The Foundry']

tools = ['Nuke10.5']

requires = ["nukeplugins-10.5",
            "ofxplugins"]

variants = []



def commands():
    """   """
    import os

    env.REZ_NUKE_VERSION.set("10.5") 
    env.NUKE_LOCATION.set('{this.root}/nuke')

    # nuke plugins dir
    # env.NUKE_PATH.append()

    # env.NUKE_TEMP_DIR.set()
    # env.OFX_PLUGIN_PATH.append()
    # env.NUKE_INTERACTIVE.append

    # env.NUKE_DISK_CACHE.set()
    # env.NUKE_DISK_CACHE_GB.set()
    # work on linux
    # env.NUKE_EXR_TEMP_DIR.set()
    
    # init.py and menu.py locations
    # env.STARTUP_PYTHON_PATH
    
    env.PATH.append("{this.root}/nuke")
    env.PATH.append("{this.root}/nuke/plugins")

    env.PATH.append("{this.root}/nuke/qtplugins/accessible")
    env.PATH.append("{this.root}/nuke/qtplugins/codecs")
    env.PATH.append("{this.root}/nuke/qtplugins/designer")
    env.PATH.append("{this.root}/nuke/qtplugins/graphicssystems")
    env.PATH.append("{this.root}/nuke/qtplugins/iconengines")
    env.PATH.append("{this.root}/nuke/qtplugins/imageformats")
    env.PATH.append("{this.root}/nuke/qtplugins/sqldrivers")

    alias("nuke", "Nuke10.5")
    alias("nukex", "nuke --nukex")
    alias("nukes", "nuke --studio")
    alias("nukestudio", "nuke --studio")
    alias("hiero", "nuke --hiero")
    alias("hierop", "nuke --player")
    alias("hieroplayer", "nuke --player")

    env.LD_LIBRARY_PATH.prepend("{this.root}/nuke")
    env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/accessible")
    env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/codecs")
    env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/designer")
    env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/graphicssystems")
    env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/iconengines")
    env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/imageformats")
    env.LD_LIBRARY_PATH.prepend("{this.root}/nuke/qtplugins/sqldrivers")

    env.PYTHONPATH.append('{this.root}/nuke/pythonextensions/site-packages')
