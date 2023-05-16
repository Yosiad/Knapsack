import random
import math

def create_random_solution(items):
    return [random.randint(0, item[3]) for item in items]

def calculate_fitness(solution, items, max_weight):
    total_weight = sum([solution[i]*items[i][1] for i in range(len(solution))])
    if total_weight > max_weight:
        return 0
    else:
        return sum([solution[i]*items[i][2] for i in range(len(solution))])

def get_neighbor(solution,items):
    neighbor = solution[:]
    index = random.randint(0, len(solution)-1)
    neighbor[index] = items[index][3]-random.randint(0,neighbor[index])
    return neighbor
def simulated_annealing(max_weight, items):
    current_solution = create_random_solution(items)
    current_fitness = calculate_fitness(current_solution, items, max_weight)
    temperature = 100
    cooling_rate = 0.99
    while temperature > 1:
        neighbor = get_neighbor(current_solution,items)
        neighbor_fitness = calculate_fitness(neighbor, items, max_weight)
        delta_fitness = neighbor_fitness - current_fitness
        if delta_fitness > 0:
            current_solution = neighbor
            current_fitness = neighbor_fitness
        else:
            probability = math.exp(delta_fitness / temperature)
            if random.random() < probability:
                current_solution = neighbor
                current_fitness = neighbor_fitness
        temperature *= cooling_rate
    return [current_fitness,current_solution]