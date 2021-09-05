from benchmark import Benchmark
import numpy as np
import matplotlib.pyplot as plt
bm = Benchmark()


class PSO():

    def __init__(self, benchmark, particles, a, b, c, r, iterations):
        self.benchmark = benchmark
        self.particles = particles
        self.iterations = iterations
        self.a = a
        self.b = b
        self.c = c
        self.plot = True
        self.R = r
        self.global_best = 1000
        self.global_best_pos = None
        self.particle_pos = np.array(
            [self.particles, self.particles, self.particles])
        self.particle_vel = np.array(
            [self.particles, self.particles, self.particles])
        self.particle_best_pos = np.copy(self.particle_pos)
        self.particle_best_val = np.zeros(len(self.particle_pos))

    def inf(self):

        if self.benchmark == 0:
            x_range, y_range, z_range = [-2, 2], [-1, 3], [0, 2500]
            def val(x, y): return bm.Rosenbrock(x, y)
        else:
            x_range, y_range, z_range = [-5, 5], [-5, 5], [0, 100]
            def val(x, y): return bm.Rastrigin(x, y)

        return x_range, y_range, z_range, val

    def plots(
            self,
            X,
            Y,
            Z,
            pos,
            best_position,
            global_best,
            iteration,
            particles):
        plt.cla()
        plt.contourf(X, Y, Z, cmap=plt.get_cmap('rainbow'))
        for i in pos:
            plt.plot(i[0], i[1], color="blue", marker="D")
        plt.plot(0, 0, 'r', marker="D")
        plt.plot(best_position[0], best_position[1], 'r')
        plt.title(
            "Particles: {}, iteration: {}, Best Value: {}\nBest Position: x={} y={}" .format(
                particles, iteration, round(
                    global_best, 7), round(
                    best_position[0], 7), round(
                    best_position[1], 7)))

    def particle_swarm(self):

        x_range, y_range, z_range, val = self.inf()
        x, y = np.meshgrid(
            np.arange(
                x_range[0], x_range[1], 0.1), np.arange(
                y_range[0], y_range[1], 0.1))
        z = np.zeros(x.shape)
        for i in np.arange(x.shape[0]):
            for j in np.arange(x.shape[1]):
                z[i, j] = val(x[i, j], y[i, j])

        self.particle_pos = np.array(
            [
                np.random.uniform(
                    x_range[0],
                    x_range[1],
                    size=self.particles),
                np.random.uniform(
                    y_range[0],
                    y_range[1],
                    size=self.particles),
                np.random.uniform(
                    z_range[0],
                    z_range[1],
                    size=self.particles)
            ]).T
        self.particle_vel = np.array(
            [
                np.random.uniform(
                    x_range[0],
                    x_range[1],
                    size=self.particles),
                np.random.uniform(
                    y_range[0],
                    y_range[1],
                    size=self.particles),
                [0] * self.particles
            ]).T

        self.particle_best_pos, self.particle_best_val = np.copy(
            self.particle_pos), np.zeros(len(self.particle_pos))
        self.global_best_pos = self.particle_best_pos[0]
        self.global_best = val(
            self.global_best_pos[0],
            self.global_best_pos[1])

    def calculate(self):
        x_range, y_range, z_range, val = self.inf()

        for i, pos in enumerate(self.particle_best_pos):
            self.particle_best_val[i] = val(pos[0], pos[1])
            if self.particle_best_val[i] < self.global_best:
                self.global_best = self.particle_best_val[i]
                self.global_best_pos = pos
        for i, pos in enumerate(self.particle_pos):
            self.particle_vel[i] = self.a * self.particle_vel[i] + self.b * self.R * (
                self.particle_best_pos[i] - pos) + self.c * self.R * (self.global_best_pos - pos)

            self.particle_pos[i] += self.particle_vel[i]
            self.particle_pos[i, 0] = min(
                max(self.particle_pos[i, 0], x_range[0]), x_range[1])
            self.particle_pos[i, 1] = min(
                max(self.particle_pos[i, 1], y_range[0]), y_range[1])
            particle_value = val(
                self.particle_pos[i, 0], self.particle_pos[i, 1])
            if particle_value <= self.particle_best_val[i]:
                self.particle_best_pos[i] = self.particle_pos[i]
                self.particle_best_val[i] = particle_value
                if self.particle_best_val[i] <= self.global_best:
                    self.global_best_pos = self.particle_best_pos[i]
                    self.global_best = self.particle_best_val[i]

        return self.global_best_pos, self.global_best, self.particle_pos

    def show(self, iteration, pso, X, Y, Z):

        global_best_pos, global_best, pos = pso.calculate()
        self.plots(
            X,
            Y,
            Z,
            pos,
            global_best_pos,
            global_best,
            iteration,
            pso.particles)
