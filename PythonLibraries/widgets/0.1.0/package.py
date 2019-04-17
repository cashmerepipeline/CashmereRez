name = 'widgets'

version = '0.1.0'

authors = ["YanGang"]

description = "InHouse widgets"

tools = []

requires = ['qtpy']


def commands():
    import os    
    libs_path = os.path.join(getenv("PYTHON_LIBS_PATH"), "widgets", "%s"%version)
    
    env.PYTHONPATH.append(os.path.join(libs_path, 'lib'))

