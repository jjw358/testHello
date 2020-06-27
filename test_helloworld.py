import pandas as pd
from helloworld import say_hello

def test_helloworld_no_params():
    assert say_hello() == "hello, world!"+pd.__version__
    
def test_helloworld_with_param():
    assert say_hello("everyone") == "hello, everyone!"+pd.__version__

