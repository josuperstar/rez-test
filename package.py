name = "requests"

version = "1.0.0"

authors = ["Jonathan Gagnon"]

requires = [
    "python-2.7+"
]

def commands():
    env.PYTHONPATH.append("{root}/python")