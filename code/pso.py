import numpy as np
import functions

f, indomain, getdomain = functions.getRipple25()
domain = getdomain()
swarm = []
w = .7
c1 = c2 = 1.4
k = 0.5
dimension = 30
particles = 30
g_best_val = float("inf")
g_best_vec = np.array([0] * dimension)
total_iterations = 0

equil = {"count":0 , "threshold":5, "equil":False, "accuracy": 3}

def random(size):
    return (domain[1] - domain[0]) * np.random.random_sample(size) + domain[0]

def initparticle():
    velocity = np.array([0] * dimension)
    position = random(dimension)
    pb_score = f(position)
    pb_vector = position
    return (velocity, position, pb_score, pb_vector)

def calc_velocity(particle):
    vel, pos, pb_sc, pb_vec = particle
    new_vector = w * vel + c1 * random(dimension) * (pb_vec - pos) + c2 * random(dimension) * (g_best_vec - pos)
    return new_vector

def clamp_velocity(vel):
    range = domain[1] - domain[0]
    vel_max = k * range
    return np.minimum(vel_max, vel)


def update_swarm_pos():
    same = True
    for i in range(0, particles):
        particle = swarm[i]
        pos = particle[1]
        v_new = calc_velocity(particle)
        pos_new = v_new + pos
        rounded = np.round(v_new, equil['accuracy'])
        same = same and (np.all(rounded == 0))
        performance = f(pos_new)
        if (performance < particle[2]) and (indomain(pos_new)):
            swarm[i] = (v_new, pos_new, performance, pos_new)
        else:
            swarm[i] = (v_new, pos_new, particle[2], particle[3])

    equil['count'] += 1 if same else 0
    equil['equil'] = (equil['count'] == equil['threshold'])


def update_gbest():
    global g_best_val
    global g_best_vec
    for particle in swarm:
        if particle[2] < g_best_val:
            g_best_val = particle[2]
            g_best_vec = particle[1]

if __name__ == '__main__':

    for i in range(particles):
        swarm.append(initparticle())

    update_gbest()
    while(not equil['equil'] and total_iterations < 5000):
        total_iterations += 1
        update_swarm_pos()
        update_gbest()

    print(g_best_val)
    print(g_best_vec)
    print("found after", total_iterations, "iterations")

    
