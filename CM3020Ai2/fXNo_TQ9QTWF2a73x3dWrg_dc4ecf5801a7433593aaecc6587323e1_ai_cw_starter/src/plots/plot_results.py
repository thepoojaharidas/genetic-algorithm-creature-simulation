import matplotlib.pyplot as plt
import csv

def plot_from_csv(filename, title):
    generations = []
    max_fitness = []
    mean_fitness = []
    min_fitness = []

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            generations.append(int(row['generation']))
            max_fitness.append(float(row['max']))
            mean_fitness.append(float(row['mean']))
            min_fitness.append(float(row['min']))

    plt.figure(figsize=(10, 6))
    plt.plot(generations, max_fitness, label='Max Fitness', marker='o')
    plt.plot(generations, mean_fitness, label='Mean Fitness', marker='o')
    plt.plot(generations, min_fitness, label='Min Fitness', marker='o')
    plt.xlabel('Generation')
    plt.ylabel('Fitness (Max Height Reached)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# List your CSVs and descriptive titles here:
files_and_titles = [
    ('results_pop10.csv', 'Evolution of Fitness: Population 10'),
    ('results_pop20.csv', 'Evolution of Fitness: Population 20'),
    ('results_pop30.csv', 'Evolution of Fitness: Population 30'),
]

for filename, title in files_and_titles:
    plot_from_csv(filename, title)
