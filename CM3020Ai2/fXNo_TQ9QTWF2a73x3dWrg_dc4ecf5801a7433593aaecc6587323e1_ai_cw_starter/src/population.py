import creature
import numpy as np
import genome as genome_module  # Add this for access to crossover/mutation

class Population:
    def __init__(self, pop_size, gene_count):
        self.creatures = [creature.Creature(
                          gene_count=gene_count) 
                          for i in range(pop_size)]

    @staticmethod
    def get_fitness_map(fits):
        fitmap = []
        total = 0
        for f in fits:
            total = total + f
            fitmap.append(total)
        return fitmap
    
    @staticmethod
    def select_parent(fitmap):
        r = np.random.rand() # 0-1
        r = r * fitmap[-1]
        for i in range(len(fitmap)):
            if r <= fitmap[i]:
                return i

    # === Add this method ===
    def evolve(self, mutation_rate=0.05):
        # Gather fitnesses
        fitnesses = [c.fitness for c in self.creatures]
        fitmap = self.get_fitness_map(fitnesses)
        # Elitism: keep the best
        best_index = fitnesses.index(max(fitnesses))
        new_creatures = [self.creatures[best_index]]  # Keep best unchanged

        while len(new_creatures) < len(self.creatures):
            # Select two parents
            idx1 = self.select_parent(fitmap)
            idx2 = self.select_parent(fitmap)
            parent1 = self.creatures[idx1]
            parent2 = self.creatures[idx2]
            # Crossover genomes
            child_dna = genome_module.Genome.crossover(parent1.dna, parent2.dna)
            # Mutate child
            child_dna = genome_module.Genome.point_mutate(child_dna, mutation_rate, amount=0.1)
            # Create new creature with child DNA
            child = creature.Creature(gene_count=len(child_dna))
            child.update_dna(child_dna)
            new_creatures.append(child)
        self.creatures = new_creatures[:len(self.creatures)]
