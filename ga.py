import random

def create_individual(items):
    return [random.randint(0, item[3]) for item in items]
def calculate_fitness(individual, items, max_weight):
    total_weight = sum([individual[i] * items[i][1] for i in range(len(individual))])
    if total_weight > max_weight:
        return 0
    else:
        return sum([individual[i] * items[i][2] for i in range(len(individual))])

def select_individuals(population, fitness, num_parents):
    parents = []
    for _ in range(num_parents):
        max_fitness = max(fitness)
        index = fitness.index(max_fitness)
        parents.append(population[index])
        fitness[index] = 0
    return parents

def crossover(parents, offspring_size):
    offspring = []
    crossover_point = len(parents[0]) // 2
    for i in range(offspring_size):
        parent1_index = i % len(parents)
        parent2_index = (i + 1) % len(parents)
        offspring1 = parents[parent1_index][:crossover_point] + parents[parent2_index][crossover_point:]
        offspring2 = parents[parent2_index][:crossover_point] + parents[parent1_index][crossover_point:]
        offspring.append(offspring1)
        offspring.append(offspring2)
    return offspring

def mutate(offspring):
    for i in range(len(offspring)):
        for j in range(len(offspring[i])):
            if random.random() < 0.05:  # Mutation rate of 5%
                offspring[i][j] = random.randint(0, offspring[i][j])
    return offspring

def genetic_algorithm(max_weight, items):
    population_size = 50
    num_parents = 10
    num_generations = 1000

    num_items = len(items)
    population = [create_individual(items) for _ in range(population_size)]

    for generation in range(num_generations):
        fitness = [calculate_fitness(individual, items, max_weight) for individual in population]
        parents = select_individuals(population, fitness, num_parents)
        offspring = crossover(parents, population_size - num_parents)
        offspring = mutate(offspring)
        population = parents + offspring

    fitness = [calculate_fitness(individual, items, max_weight) for individual in population]
    max_fitness = max(fitness)
    max_index = fitness.index(max_fitness)
    return [max_fitness, population[max_index]]