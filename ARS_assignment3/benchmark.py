import numpy as np


class Rastrigin:

    def rastrigin_function(self, *X):
        z = 10 * 2 + sum([(np.square(x) - 10 * np.cos(2 * np.pi * x))
                         for x in X])
        return z

    def evaluate_function(self, position):
        z = 10 + np.sum([(np.square(x) - 10 * np.cos(2 * np.pi * x)) for x in position])
        return z

    def get_surface(self, resolution=100, boundary=5.12):
        X = np.linspace(-boundary, boundary, resolution)
        Y = np.linspace(-boundary, boundary, resolution)
        X, Y = np.meshgrid(X, Y)
        Z = self.rastrigin_function(X, Y)
        return np.stack((X, Y, Z))


class Rosenbrock:

    def __init__(self):
        self.a = 0
        self.b = 100

    def rosenbrock_function(self, *X):
        x = X[0]
        y = X[1]
        z = (self.a - x) ** 2 + self.b * (y - x ** 2) ** 2
        return z

    def evaluate_function(self, position):
        x = position[0]
        y = position[1]
        z = (self.a - x) ** 2 + self.b * (y - x ** 2) ** 2
        return z

    def get_surface(self, resolution=100, boundary=5.12):
        X = np.linspace(-boundary, boundary, resolution)
        Y = np.linspace(-boundary, boundary, resolution)
        X, Y = np.meshgrid(X, Y)
        Z = self.rosenbrock_function(X, Y)
        return np.stack((X, Y, Z))
