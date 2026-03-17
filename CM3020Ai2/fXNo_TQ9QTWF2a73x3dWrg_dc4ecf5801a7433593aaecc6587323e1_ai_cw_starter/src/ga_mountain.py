import pybullet as p
import pybullet_data
import time
import numpy as np
import random
import creature
import population
import csv

def setup_env():
    p.resetSimulation()
    p.setGravity(0, 0, -10)
    arena_size = 20
    def make_arena(arena_size=10, wall_height=1):
        wall_thickness = 0.5
        floor_collision_shape = p.createCollisionShape(shapeType=p.GEOM_BOX, halfExtents=[arena_size/2, arena_size/2, wall_thickness])
        floor_visual_shape = p.createVisualShape(shapeType=p.GEOM_BOX, halfExtents=[arena_size/2, arena_size/2, wall_thickness], rgbaColor=[1, 1, 0, 1])
        floor_body = p.createMultiBody(baseMass=0, baseCollisionShapeIndex=floor_collision_shape, baseVisualShapeIndex=floor_visual_shape, basePosition=[0, 0, -wall_thickness])
        wall_collision_shape = p.createCollisionShape(shapeType=p.GEOM_BOX, halfExtents=[arena_size/2, wall_thickness/2, wall_height/2])
        wall_visual_shape = p.createVisualShape(shapeType=p.GEOM_BOX, halfExtents=[arena_size/2, wall_thickness/2, wall_height/2], rgbaColor=[0.7, 0.7, 0.7, 1])
        # Four walls
        p.createMultiBody(baseMass=0, baseCollisionShapeIndex=wall_collision_shape, baseVisualShapeIndex=wall_visual_shape, basePosition=[0, arena_size/2, wall_height/2])
        p.createMultiBody(baseMass=0, baseCollisionShapeIndex=wall_collision_shape, baseVisualShapeIndex=wall_visual_shape, basePosition=[0, -arena_size/2, wall_height/2])
        wall_collision_shape = p.createCollisionShape(shapeType=p.GEOM_BOX, halfExtents=[wall_thickness/2, arena_size/2, wall_height/2])
        wall_visual_shape = p.createVisualShape(shapeType=p.GEOM_BOX, halfExtents=[wall_thickness/2, arena_size/2, wall_height/2], rgbaColor=[0.7, 0.7, 0.7, 1])
        p.createMultiBody(baseMass=0, baseCollisionShapeIndex=wall_collision_shape, baseVisualShapeIndex=wall_visual_shape, basePosition=[arena_size/2, 0, wall_height/2])
        p.createMultiBody(baseMass=0, baseCollisionShapeIndex=wall_collision_shape, baseVisualShapeIndex=wall_visual_shape, basePosition=[-arena_size/2, 0, wall_height/2])
    make_arena(arena_size=arena_size)
    mountain_position = (0, 0, -1)
    mountain_orientation = p.getQuaternionFromEuler((0, 0, 0))
    p.setAdditionalSearchPath('shapes/')
    mountain = p.loadURDF("gaussian_pyramid.urdf", mountain_position, mountain_orientation, useFixedBase=1)

def evaluate_creature(genome, sim_steps=1000):
    # Save creature as URDF
    with open('test.urdf', 'w') as f:
        f.write(genome.to_xml())
    # Load into sim
    start_pos = (0, 0, 10)
    creature_id = p.loadURDF('test.urdf', start_pos)
    max_height = 0

    motors = genome.get_motors()
    num_joints = p.getNumJoints(creature_id)
    num_motors = len(motors)
    # print("Num joints:", num_joints, "Num motors:", num_motors)

    for step in range(sim_steps):
        # Safely loop over the number of available motors and joints
        for j in range(min(num_joints, num_motors)):
            motor_output = motors[j].get_output()  # Value between -1 and 1
            target_pos = motor_output * 1.5  # Tweak scaling as needed
            p.setJointMotorControl2(
                bodyUniqueId=creature_id,
                jointIndex=j,
                controlMode=p.POSITION_CONTROL,
                targetPosition=target_pos
            )

        p.stepSimulation()
        pos, _ = p.getBasePositionAndOrientation(creature_id)
        z = pos[2]
        if z > max_height:
            max_height = z
        # time.sleep(1./240.)  # Uncomment only if you want slow motion

    p.removeBody(creature_id)
    return max_height

def main():
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    # === CHANGE THESE PARAMETERS FOR YOUR EXPERIMENTS ===
    pop_size = 30         # Population size
    generations = 20      # Number of generations
    sim_steps = 1000      # Simulation steps per creature
    gene_count = 3        # Gene count per creature

    pop = population.Population(pop_size=pop_size, gene_count=gene_count)

    log = []
    for gen in range(generations):
        print(f"=== Generation {gen} ===")
        setup_env()  # Reset mountain/arena for every generation
        fitnesses = []
        for genome in pop.creatures:
            fitness = evaluate_creature(genome, sim_steps=sim_steps)
            genome.fitness = fitness
            fitnesses.append(fitness)
        # GA: Evolve population to next generation
        pop.evolve()
        # Log results
        log.append((gen, max(fitnesses), np.mean(fitnesses), min(fitnesses)))
        print(f"Best: {max(fitnesses):.2f}, Mean: {np.mean(fitnesses):.2f}, Worst: {min(fitnesses):.2f}")

    # Write results to CSV for later plotting
    with open('results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['generation', 'max', 'mean', 'min'])
        writer.writerows(log)

    print("Evolution finished. Results saved to results.csv. Press Enter to exit.")
    input()

if __name__ == "__main__":
    main()
