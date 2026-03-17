import matplotlib.pyplot as plt
import csv

def load_results(filename):
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
    return generations, max_fitness, mean_fitness, min_fitness

# List your files and labels
files_and_labels = [
    ('results_pop10.csv', 'Population 10'),
    ('results_pop20.csv', 'Population 20'),
    ('results_pop30.csv', 'Population 30'),
]

plt.figure(figsize=(10, 6))

# Plot max fitness for each experiment
for filename, label in files_and_labels:
    gens, max_f, mean_f, min_f = load_results(filename)
    plt.plot(gens, max_f, marker='o', label=f'Max Fitness ({label})')

plt.xlabel('Generation')
plt.ylabel('Fitness (Max Height Reached)')
plt.title('Comparison of Max Fitness: Different Population Sizes')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# (Optional) Plot mean fitness for each experiment
plt.figure(figsize=(10, 6))
for filename, label in files_and_labels:
    gens, max_f, mean_f, min_f = load_results(filename)
    plt.plot(gens, mean_f, marker='o', label=f'Mean Fitness ({label})')

plt.xlabel('Generation')
plt.ylabel('Fitness (Mean Height Reached)')
plt.title('Comparison of Mean Fitness: Different Population Sizes')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
