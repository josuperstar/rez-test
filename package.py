name = "hello_world_test1"

version = "1.0.3"

authors = [
    "ajohns"
]

description = \
    """
    Python-based hello world example package.
    """

tools = [
    "hello"
]

requires = [
    "python-2.7+"
]

uuid = "examples.hello_world_py"

def commands():
    env.PYTHONPATH.append("{root}/python")
    env.PATH.append("{root}/bin")
