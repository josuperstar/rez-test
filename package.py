name = "hello_world_test1"

version = "1.0.2"

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
    "python"
]

uuid = "examples.hello_world_py"

def commands():
    env.PYTHONPATH.append("{root}/python")
    env.PATH.append("{root}/bin")
