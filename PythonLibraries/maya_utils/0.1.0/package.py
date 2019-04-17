name = 'maya_utils'

version = '0.1.0'

authors = [
    "YanGang",
    "YanGang"
]

description = \
    """
    maya utils
    """

tools = []

requires = ['maya-2016']



def commands():
    import os
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "maya_utils", "%s"%version)
    
    env.PYTHONPATH.append(os.path.join(libs_path, "lib"))


