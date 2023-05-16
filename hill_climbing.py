import random

def create_random_solution(num_items):
    return [random.randint(0, 1) for _ in range(num_items)]

def calculate_fitness(solution, items, max_weight):
    total_weight = sum([solution[i]*items[i][1] for i in range(len(solution))])
    if total_weight > max_weight:
        return 0
    else:
        return sum([solution[i]*items[i][2] for i in range(len(solution))])

def get_neighborhood(solution):
    neighborhood = []
    for i in range(len(solution)):
        neighbor = solution[:]
        neighbor[i] = neighbor[i]+1 
        neighborhood.append(neighbor)
        if neighbor[i]>2: neighbor[i]-2
    return neighborhood

def hill_climbing(max_weight, items):
    num_items = len(items)
    current_solution = create_random_solution(num_items)
    current_fitness = calculate_fitness(current_solution, items, max_weight)
    while True:
        neighborhood = get_neighborhood(current_solution)
        best_neighbor = current_solution 
        best_fitness = current_fitness 
        for neighbor in neighborhood:
            neighbor_fitness = calculate_fitness(neighbor, items, max_weight)
            if neighbor_fitness > best_fitness:
                best_neighbor = neighbor
                best_fitness = neighbor_fitness
        if best_fitness == current_fitness:
            break
        current_solution = best_neighbor
        current_fitness = best_fitness
    return  [current_fitness,current_solution]