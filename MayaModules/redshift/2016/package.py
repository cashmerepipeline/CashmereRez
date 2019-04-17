# -*- coding: utf-8 -*-

name = 'redshift'

version = '1.3.9'

author = ['redshift']

tools = []

requires = []

variants = [
    ['platform-windows'],
    
]




def commands():
    """   """
    import os

    env.redshift_LICENSE.set("5053@rlm.cashmere.com")

    module_path = getenv("MAYA_MODDULE_PATH")
    redshift_module_path = os.path.join(module_path, "redshift/2016".replace('/', os.sep))

    env.REDSHIFT_COREDATAPATH.set(redshift_module_path)
    env.REDSHIFT_PROCEDURALSPATH = os.path.join(getenv("REDSHIFT_COREDATAPATH"), "Procedurals")

    env.REDSHIFT_SCRIPT_PATH.set(os.path.join(getenv("REDSHIFT_COREDATAPATH"), "Plugins/Maya/Common/scripts".replace('/', os.sep)))
    env.REDSHIFT_XBMLANGPATH.set(os.path.join(getenv("REDSHIFT_COREDATAPATH"), "Plugins/Maya/Common/icons".replace('/', os.sep)))
    env.REDSHIFT_RENDER_DESC_PATH.set(os.path.join(getenv("REDSHIFT_COREDATAPATH"), "Plugins/Maya/Common/rendererDesc".replace('/', os.sep)))
    env.REDSHIFT_CUSTOM_TEMPLATE_PATH.set(os.path.join(getenv("REDSHIFT_COREDATAPATH"), "Plugins/Maya/Common/scripts/NETemplates".replace('/', os.sep)))

    env.REDSHIFT_PLUG_IN_PATH.set(os.path.join(redshift_module_path, 'Plugins/Maya/2016/nt-x86-64'.replace('/', os.sep)))

    env.REDSHIFT_MAYAEXTENSIONSPATH.set(os.path.join(getenv("REDSHIFT_PLUG_IN_PATH"), "extensions"))

    env.MAYA_PLUG_IN_PATH.append(getenv("REDSHIFT_PLUG_IN_PATH"))

    env.MAYA_SCRIPT_PATH.append(getenv("REDSHIFT_SCRIPT_PATH"))
    env.XBMLANGPATH.append(getenv("REDSHIFT_XBMLANGPATH"))
    env.MAYA_RENDER_DESC_PATH.append(getenv("REDSHIFT_RENDER_DESC_PATH"))
    env.MAYA_CUSTOM_TEMPLATE_PATH.append(getenv("REDSHIFT_CUSTOM_TEMPLATE_PATH"))

    env.PATH.append(os.path.join(getenv("REDSHIFT_COREDATAPATH"), "bin"))
    env.PATH.append(getenv("REDSHIFT_PLUG_IN_PATH"))
    env.PYTHONPATH.append(getenv("REDSHIFT_SCRIPT_PATH"))

    env.LD_LIBRARY_PATH.prepend(os.path.join(getenv("REDSHIFT_COREDATAPATH"), "bin"))
    env.LD_LIBRARY_PATH.prepend(getenv("REDSHIFT_PLUG_IN_PATH"))
    env.LD_LIBRARY_PATH.prepend(getenv("REDSHIFT_MAYAEXTENSIONSPATH"))