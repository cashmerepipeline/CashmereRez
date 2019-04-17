name = 'desktop'

version = '0.0.1'

authors = [
    "YanGang"
]

description = \
    """
    desktop config
    """

tools = []

requires = ['pyside', 'pillow', 'pyaml']



def commands():
    import os
    desktop_path = os.path.join(getenv("INHOUSE_PATH"), "desktop", "%s"%version)
    env.PATH.append(os.path.join(desktop_path, 'bin'))

    env.DESKTOP_SETUP = os.path.join(desktop_path, 'bin').replace('\\', '/')
    env.PYTHONPATH.append(os.path.join(desktop_path,'lib'))


