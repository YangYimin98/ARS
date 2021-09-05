import numpy as np


class Benchmark():

    def __init__(self):
        self.a = 0
        self.b = 100
        self.plot = True

    def Rosenbrock(self, x, y):

        z = (self.a - x) ** 2 + self.b * (y - x ** 2) ** 2
        return z

    def Rastrigin(self, x1, x2):

        z = 10 * 2 + (x1 ** 2 - 10 * np.cos(2 * np.pi * x1) +
                      x2 ** 2 - 10 * np.cos(2 * np.pi * x2))
        return z

    def surface(self, s):
        if s == 0:
            res = 0.05
            X = np.arange(-2, 2 + res, res)
            Y = np.arange(-2, 3 + res, res)
            X, Y = np.meshgrid(X, Y)
            Z = self.Rosenbrock(X, Y)
        else:
            X = np.linspace(-5.12, 5.12, 100)
            Y = np.linspace(-5.12, 5.12, 100)
            X, Y = np.meshgrid(X, Y)
            Z = self.Rastrigin(X, Y)
        return X, Y, Z
