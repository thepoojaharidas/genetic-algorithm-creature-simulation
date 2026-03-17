# genetic-algorithm-creature-simulation

# Evolutionary Robotics – Mountain Climbing Simulation
**Python | PyBullet | Genetic Algorithm | Matplotlib**

## Overview
A full evolutionary robotics pipeline that evolves virtual creatures 
to climb a 3D mountain terrain using a Genetic Algorithm (GA). 
Creatures are procedurally generated, physically simulated, and 
iteratively improved across generations through selection, 
crossover, and mutation.

## What it does
- Generates virtual creatures with randomised morphologies (body 
  structure + joints) encoded as URDF files
- Simulates each creature in a 3D PyBullet physics environment 
  on a Gaussian pyramid mountain
- Evaluates fitness based on maximum height reached during simulation
- Evolves the population across generations using a genetic algorithm
- Logs results (max, mean, min fitness per generation) to CSV
- Visualises evolutionary progress using matplotlib

## Key Experiments

### Experiment 1: Evolving Motor Control Only (Fixed Body)
- Fixed morphology; evolved only motor parameters
- Result: Slower improvement, earlier plateau — body structure 
  limits maximum performance

### Experiment 2: Evolving Morphology Only (Fixed Motor Control)
- Fixed motor control; evolved only body structure
- Result: Minimal fitness gain — coordinated control is essential 
  for effective climbing

### Experiment 3: Co-Evolution of Morphology + Control (Best)
- Evolved both body structure and motor control simultaneously
- Result: Highest and most consistent fitness improvements across 
  all population sizes

### Population Size Comparison (10 / 20 / 30)
- Larger populations showed more stable mean fitness and higher 
  peak performance over 20 generations

## Results Summary

| Encoding Scheme         | Max Fitness | Mean Fitness | Outcome          |
|-------------------------|-------------|--------------|------------------|
| Morphology + Control    | High        | High         | Best performance |
| Motor Control Only      | Moderate    | Moderate     | Limited by body  |
| Morphology Only         | Low         | Low          | Rarely improved  |

## Tech Stack
- **Python 3**
- **PyBullet** — 3D physics simulation
- **NumPy** — numerical computation
- **Matplotlib** — fitness visualisation
- **CSV** — results logging

## How to Run
```bash
pip install pybullet numpy matplotlib
python ga_mountain.py


## Key Learnings
- Co-adaptation of form and function is critical in embodied AI tasks
- Population size directly influences diversity and convergence speed
- Procedural URDF generation enables scalable morphology search
- Physics-based fitness evaluation provides realistic performance signals

## References
- Silver et al. (2016) — AlphaGo, Nature
- Yannakakis & Togelius (2018) — Artificial Intelligence and Games
- Bostrom (2014) — Superintelligence

