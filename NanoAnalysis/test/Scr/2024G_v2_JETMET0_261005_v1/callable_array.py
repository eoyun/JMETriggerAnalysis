import numpy

class callable_numpy:
    def __init__(self, array):
        self.array = array

    def __call__(self,index):
        return self.array[index]

