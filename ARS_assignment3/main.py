from evolutionary_algorithm import *
import matplotlib.pyplot as plt
from matplotlib import animation
from benchmark import Rastrigin, Rosenbrock


def run(iteration):
    positions = ea.gene_pool()

    fitness = [function.evaluate_function(pos) for pos in positions]
    ea.fitness_function(fitness)
    best_position, best_fitness, population_size = ea.selection()

    surface = function.get_surface()
    plot(
        surface,
        positions,
        best_fitness,
        best_position,
        iteration,
        population_size)


def plot(
        surface,
        positions,
        best_fitness,
        best_position,
        iteration,
        population_size):
    plt.cla()
    plt.contourf(
        surface[0],
        surface[1],
        surface[2],
        levels=15,
        cmap=plt.get_cmap('rainbow'))
    plt.scatter(0, 0, 20, color="black", marker="o")
    x, y, z = zip(*positions)
    plt.scatter(x, y, 3, 'k', edgecolors='face')
    plt.scatter(best_position[0], best_position[1], 20, 'r', edgecolors='face')
    plt.title(
        "Population: {}, Iteration: {}, Fitness: {:.6f}".format(
            population_size,
            iteration,
            best_fitness))


def info(index):
    global function
    if index == 0:
        function = Rastrigin()
    elif index == 1:
        function = Rosenbrock()
    return function


ELITISM = 0.1
POPULATION_SIZE = 200
RATE = 0.8
SIGMA = 0.1
DECAY = 0.999
LIMITATION = 0.001
ITERATION = 300
BOUNDARY_X = BOUNDARY_Y = 5.12
DNA_BOUNDARY = (-BOUNDARY_X, BOUNDARY_X)
pos_x = np.random.uniform(-BOUNDARY_X, BOUNDARY_X)
pos_y = np.random.uniform(-BOUNDARY_X, BOUNDARY_X)
pos_z = np.random.uniform(0, 100)
DNA_INITIAL_POSITION = [pos_x, pos_y, pos_z]

info(1)
ea = EA(
    len(DNA_INITIAL_POSITION),
    DNA_BOUNDARY,
    DNA_INITIAL_POSITION,
    ELITISM,
    POPULATION_SIZE,
    RATE,
    SIGMA,
    DECAY,
    LIMITATION)
fig = plt.figure(figsize=(8, 8))
ani = animation.FuncAnimation(fig, run, frames=ITERATION)
plt.show()
