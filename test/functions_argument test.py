import inspect

def test_functions(a, b, c, d):
    pass

print(inspect.signature(test_functions))

class hi:
    def __init__(self, a, b):
        pass

test = hi(2,3)

print(inspect.signature(hi.__init__))