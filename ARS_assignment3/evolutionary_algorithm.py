import numpy as np


class EA:
    def __init__(
            self,
            dna_size,
            dna_boundary,
            dna_start_position=None,
            elitism=0.01,
            population_size=200,
            mutation_rate=0.01,
            mutation_sigma=0.1,
            mutation_decay=0.999,
            mutation_limit=0.01,
            mutation=None,
            crossover=None):
        self.population = self._initialize_propulation(
            dna_size, mutation_sigma, dna_start_position, population_size)
        self.population = np.clip(
            self.population,
            dna_boundary[0],
            dna_boundary[1])
        self.fitness = np.zeros_like(self.population)
        self.best_dna = None
        self.best_fitness = None
        self.dna_boundary = dna_boundary
        self.elitism = elitism
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.mutation_sigma = mutation_sigma
        self.mutation_decay = mutation_decay
        self.mutation_limit = mutation_limit
        self.mutation = mutation
        self.crossover = crossover

    def _initialize_propulation(
            self,
            dna_size,
            dna_sigma,
            dna_start_position,
            population_size):
        chromosome = np.random.standard_normal(
            (population_size, dna_size)) * dna_sigma
        # print(chromesome)
        return chromosome + dna_start_position

    def gene_pool(self):
        self.mutation_sigma *= self.mutation_decay
        self.mutation_sigma = np.maximum(
            self.mutation_sigma, self.mutation_limit)
        return self.population

    def fitness_function(self, fitness):
        assert len(fitness) == len(self.fitness)
        self.fitness = np.array(fitness)
        fitness_indices = self.fitness.argsort()
        sorted_fitness = self.fitness[fitness_indices]
        fitness_weighting = np.maximum(
            0, 1 - sorted_fitness / self.fitness.sum())
        fitness_weighting /= fitness_weighting.sum()
        sorted_population = self.population[fitness_indices]

        self.best_dna = sorted_population[0]
        self.best_fitness = sorted_fitness[0]

        amount_new = int((1 - self.elitism) * len(self.population))
        new_population = []
        for _ in range(amount_new):
            i0 = np.random.choice(
                sorted_population.shape[0],
                p=fitness_weighting)
            i1 = np.random.choice(
                sorted_population.shape[0],
                p=fitness_weighting)
            new_dna = self.__crossover(
                self.population[i0],
                self.population[i1],
                crossover_type='Uniform')
            new_dna = self.__mutation(
                new_dna, self.mutation_sigma, self.mutation_rate)
            new_population.append(new_dna)

        amount_old = self.population_size - amount_new
        new_population = np.array(new_population +
                                  sorted_population[:amount_old].tolist())
        assert new_population.shape == self.population.shape
        self.population = np.clip(
            new_population,
            self.dna_boundary[0],
            self.dna_boundary[1])

    def selection(self):
        return self.best_dna, self.best_fitness, self.population_size

    def __mutation(self, dna, mutation_sigma, mutation_rate):
        if self.mutation is not None:
            return self.mutation(dna)

        if np.random.random_sample() < mutation_rate:
            dna += np.random.standard_normal(size=dna.shape) * mutation_sigma
        return dna

    def __crossover(self, dna_mother, dna_father, crossover_type):
        assert len(dna_mother) == len(dna_father)
        global offspring
        if crossover_type == 'Uniform':
            if self.crossover is not None:
                return self.crossover(dna_mother, dna_father)
            offspring = np.copy(dna_mother)
            indices = np.where(np.random.randint(2, size=offspring.size))
            offspring[indices] = dna_father[indices]

        elif crossover_type == 'Arithmetic':
            if self.crossover is not None:
                return self.crossover(dna_mother, dna_father)
            offspring = np.copy(dna_mother)
            rand = np.random.uniform(0, 1)
            for indices in range(offspring.size):
                offspring[indices] = (
                    dna_mother[indices] * rand + (1 - rand) * dna_father[indices])
        # print(offspring)
        # print("---------------------")
        return offspring
