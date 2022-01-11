import numpy as np
import matplotlib.pyplot as plt


def get_acceleration(pos, mass, G, softening):
    # r = [x, y, z]
    x = pos[:, 0:1]  # all x coordinates
    y = pos[:, 1:2]  # all y coordinates
    z = pos[:, 2:3]  # all z coordinates

    # pairwise distances
    dx = x.T - x
    dy = y.T - y
    dz = z.T - z

    inv_r3 = (dx**2 + dy**2 + dz**2 + softening**2)
    inv_r3[inv_r3 > 0] = inv_r3[inv_r3 > 0]**(-1.5)

    ax = G * (dx * inv_r3) @ mass  # @ is matrix multiplication
    ay = G * (dy * inv_r3) @ mass
    az = G * (dz * inv_r3) @ mass

    a = np.hstack((ax, ay, az))

    return a


def get_energy(pos, vel, mass, G):

    # Kinetic Energy
    KE = 0.5 * np.sum(np.sum(mass*vel**2))

    # Potential Energy
    x = pos[:, 0:1]
    y = pos[:, 1:2]
    z = pos[:, 2:3]
    dx = x.T - x
    dy = y.T - y
    dz = z.T - z

    inv_r = np.sqrt(dx**2 + dy**2 + dz**2)
    inv_r[inv_r > 0] = 1.0/inv_r[inv_r > 0]
    # upper-triangularize
    PE = G * np.sum(np.sum(np.triu(-(mass*mass.T)*inv_r, 1)))
    return KE, PE


def main():
    N = 200  # particles
    t = 0
    t_end = 10.0
    dt = 0.01
    softening = 0.1
    G = 1.0
    plot_real_time = True
    np.random.seed(42)
    mass = 20.0*np.ones((N, 1))/N  # total mass of particles is 20
    pos = np.random.randn(N, 3)  # random positions
    vel = np.random.randn(N, 3)  # random velocities
    # convert to CoM frame
    vel -= np.mean(mass * vel, 0) / np.mean(mass)

    acc = get_acceleration(pos, mass, G, softening)  # init acceleration

    KE, PE = get_energy(pos, vel, mass, G)  # init energy

    Nt = int(np.ceil(t_end / dt))

    # save data for plotting
    pos_save = np.zeros((N, 3, Nt + 1))
    pos_save[:, :, 0] = pos
    KE_save = np.zeros(Nt + 1)
    KE_save[0] = KE
    PE_save = np.zeros(Nt + 1)
    PE_save[0] = PE
    t_all = np.arange(Nt + 1) * dt

    # prepare plotting
    fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
    # main loop
    for i in range(Nt):
        # 1/2 kick
        vel += acc * dt/2.0

        # drift
        pos += vel * dt

        # update accelerations
        acc = get_acceleration(pos, mass, G, softening)

        # 1/2 kick
        vel += acc * dt/2.0

        # update time
        t += dt

        # get energy of system
        KE, PE = get_energy(pos, vel, mass, G)

        # save
        pos_save[:, :, i+1] = pos
        KE_save[i+1] = KE
        PE_save[i+1] = PE

        # plotting
        if plot_real_time or (i == Nt-1):
            plt.cla()
            xx = pos_save[:, 0, max(i-50, 0):i+1]
            yy = pos_save[:, 1, max(i-50, 0):i+1]
            plt.scatter(xx, yy, s=1, color='cornflowerblue', alpha=0.5)
            plt.scatter(pos[:, 0], pos[:, 1], s=20, color='blue')
            ax.set(xlim=(-2, 2), ylim=(-2, 2))
            ax.set_aspect('equal', 'box')
            ax.set_xticks([-2, -1, 0, 1, 2])
            ax.set_yticks([-2, -1, 0, 1, 2])

            # plt.sca(ax2)
            # plt.cla()
            # plt.scatter(t_all, KE_save, color='red', s=1,
            #             label='KE' if i == Nt-1 else "")
            # plt.scatter(t_all, PE_save, color='blue', s=1,
            #             label="PE" if i == Nt-1 else "")
            # plt.scatter(t_all, KE_save + PE_save, color='white',
            #             s=1, label='Etot' if i == Nt-1 else "")
            # ax2.set(xlim=(0, t_end), ylim=(-300, 300))
            # ax2.set_aspect(0.007)
            plt.pause(0.001)

    # plt.sca(ax2)
    # plt.xlabel('time')
    # plt.ylabel('energy')
    # ax2.legend(loc='upper right')
    plt.savefig('nbody.png', dpi=240)
    plt.show()
    return 0

    print("\n\nDONE\n\n")


if __name__ == "__main__":
    main()
