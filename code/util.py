import numpy as np


def average_particle(swarm):
    dim = np.size(swarm[0][1])
    average = np.array([0] * dim)
    for particle in swarm:
        average += particle[1]
    average /= dim
    return average

def calc_diversity(swarm):
    average = average_particle(swarm)
    for particle in swarm:
        pass
    pass