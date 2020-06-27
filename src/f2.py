import numpy as np

def say_np(name=None):
    return ("hello, world!" if (name is None) else f"hello, {name}!")+np.__version__
