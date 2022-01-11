import numpy as np
import matplotlib.pyplot as plt
from body import Body
import random
import webcolors
from time import time


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def circlev(rx, ry):
    solar_mass = 1.98892e30
    r2 = np.sqrt(rx**2 + ry**2)
    numerator = (6.67e-11)*1e6*solar_mass
    return np.sqrt(numerator/r2)


def initialize_bodies(N):
    radius = 1e18
    solar_mass = 1.98892e30
    bodies = [None]*N
    for i in range(N):
        exponential = - np.log(1 - random.random()) / (-1.8)
        px = 1e18 * exponential * \
            (0.5 - random.random()) + (random.randint(-2, 2) * 1e17)
        py = 1e18 * exponential * \
            (0.5 - random.random()) + (random.randint(-2, 2) * 1e17)
        magv = circlev(px, py)
        absangle = np.arctan(np.abs(py/px))
        thetav = np.pi/2-absangle
        phiv = random.random()*np.pi
        vx = -1 * float(np.sign(py))*np.cos(thetav)*magv
        vy = float(np.sign(px))*np.sin(thetav)*magv
        if (random.random() <= 0.5):
            vx = -vx
            vy = -vy
        mass = random.random() * solar_mass * 10 + 1e20
        red = int(np.floor(mass*254/(solar_mass*10+1e20)))
        green = int(np.floor(mass*254/(solar_mass*10+1e20)))
        blue = 255
        color = [red, green, blue]
        softening = N**(-0.3)
        bodies[i] = Body(px, py, vx, vy, mass, softening, color)
        left_x = -2e17
        right_x = 2e17
    bodies[0] = Body(0, 0, 0, 0, 3e6*solar_mass,
                     softening, color=[255, 165, 0])
    # bodies[-1] = Body(right_x, 0, 0, 0, 4e6*solar_mass,  # To see what happens with two supermassive bodies
    #                   softening, color=[255, 165, 0])
    return bodies


def add_forces(bodies, dt):
    for i in range(len(bodies)):
        bodies[i].reset_force()
        for j in range(len(bodies)):
            if i != j:
                bodies[i].add_force(bodies[j])
    for i in range(len(bodies)):
        bodies[i].update(dt)


def get_positions(bodies):
    N = len(bodies)
    pos = np.zeros((N, 2))
    for i in range(N):
        x = bodies[i].rx
        y = bodies[i].ry
        pos[i][0] = x
        pos[i][1] = y
    return pos


def get_colors(bodies, num):
    N = len(bodies)
    colors = []
    for i in range(N):
        color = bodies[i].color
        colors.append(color)
    colors = np.array(colors)
    colors = np.tile(colors, (num, 1))
    return colors


def main():
    N = 200
    t = 0
    t_end = 1e13
    dt = 1e11
    bodies = initialize_bodies(N)
    G = 6.673e-11
    plot_real_time = True
    np.random.seed(42)

    Nt = int(np.ceil(t_end/dt))
    pos_save = np.zeros((N, 2, Nt+1))
    pos = get_positions(bodies)
    pos_save[:, :, 0] = pos

    fig, ax = plt.subplots(figsize=(8, 8), dpi=80)

    start_time = time()
    for t in range(Nt):
        add_forces(bodies, dt)
        pos = get_positions(bodies)
        pos_save[:, :, t+1] = pos
        plt.cla()
        xx = pos_save[:, 0, max(t-50, 0):t+1]
        yy = pos_save[:, 1, max(t-50, 0):t+1]
        colors = get_colors(bodies, 1)
        trailing_colors = get_colors(bodies, xx.shape[1])
        plt.scatter(xx, yy, s=1, color='cornflowerblue', alpha=0.5)
        plt.scatter(pos[0, 0], pos[0, 1], s=80, color='orange')
        plt.scatter(pos[1:, 0], pos[1:, 1], c=colors[1:]/255.0, s=20)
        # plt.scatter(pos[1:-1, 0], pos[1:-1, 1], c=colors[1:-1]/255.0, s=20) # for second very massive body
        # plt.scatter(pos[-1, 0], pos[-1, 1], s=100, color='orange')
        ax.set_aspect('equal', 'box')
        ax.set(xlim=[-0.5e18, 0.5e18], ylim=[-0.5e18, 0.5e18])
        plt.pause(0.001)
    end_time = time()
    total_time = end_time - start_time
    print("The simulation with {} particles took {} seconds".format(N, total_time))
    plt.savefig('nbody.png', dpi=240)
    plt.show()
    print("\n\nDONE\n\n")


if __name__ == "__main__":
    main()
