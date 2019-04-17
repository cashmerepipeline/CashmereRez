name = 'workflow'

version = '0.1.0'

authors = [
    "YanGang"
]

description = \
    """
    workflow
    """

tools = []

requires = ['maya_utils', 'scandir', 'pyaml', 'shotgun_utils', 'widgets']



def commands():
    import os
    workflow_path = os.path.join(getenv("INHOUSE_PATH"), "workflow",  "%s"%version)
    
    env.PATH.append(os.path.join(workflow_path, 'bin'))
    env.PYTHONPATH.append(os.path.join(workflow_path,'lib'))

