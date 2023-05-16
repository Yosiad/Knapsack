import random

# Set the number of items to generate
num_items = 20

# Set the maximum weight for the knapsack
max_weight = 200

# Generate a list of item names
item_names = ["Item {}".format(i) for i in range(1, num_items+1)]

# Generate random weights and values for each item
item_weights = [round(random.uniform(0.01, 5.0), 2) for i in range(num_items)]
item_values = [random.randint(1, 1000) for i in range(num_items)]
item_counts = [random.randint(1, 10) for i in range(num_items)]

# Write the data to a file
with open("my-file.txt", "w") as f:
    # Write the maximum weight to the first line
    f.write("{}\n".format(max_weight))
    
    # Write the item headers to the second line
    f.write("Item,  weight,   value,  num_items\n")
    
    # Write the item details to subsequent lines
    for i in range(num_items):
        f.write("{},  {},  {},  {}\n".format(item_names[i], item_weights[i], item_values[i], item_counts[i]))

