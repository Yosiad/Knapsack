import argparse
from ga import genetic_algorithm
from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing
import timeit


def read_input_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        max_weight = int(lines[0])
        items = []
        for line in lines[2:]:
            name, weight, value, num_items = line.strip().split(',')
            items.append((name.strip(), float(weight), int(value), int(num_items)))
    return max_weight, items


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm', type=str, help='Algorithm to use (ga, hc, or sa)', required=True)
    parser.add_argument('--file', type=str, help='Input file name', required=True)
    args = parser.parse_args()

    max_weight, items = read_input_file("my-file.txt")

    if args.algorithm == 'ga':
        result = genetic_algorithm(max_weight, items) +[timeit.timeit("genetic_algorithm(max_weight, items)", number=10, globals=globals())/10]
    elif args.algorithm == 'hc':
        result = hill_climbing(max_weight, items)+[timeit.timeit("hill_climbing(max_weight, items)", number=10, globals=globals())/10]
    elif args.algorithm == 'sa':
        result = simulated_annealing(max_weight, items)+[timeit.timeit("simulated_annealing(max_weight, items)", number=10, globals=globals())/10]
    else:
        raise ValueError(f'Invalid algorithm: {args.algorithm}')

    print(f'Maximum value: {result[0]}')
    print(f'Selected items: {result[1]}')
    print(f'Excusion time: {result[2]}')
 