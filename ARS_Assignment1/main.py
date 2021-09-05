from PSO import *
from matplotlib import animation

if __name__ == '__main__':
    fig = plt.figure(figsize=(10, 10))
    benchmark = 0
    bm = Benchmark()
    pso = PSO(benchmark=benchmark, particles=100, a=0.9, b=2,
              c=2, r=np.random.uniform(0, 1), iterations=100)
    pso.particle_swarm()
    X, Y, Z = bm.surface(benchmark)
    anim = animation.FuncAnimation(fig, pso.show, fargs=(pso, X, Y, Z))
    plt.show()
