import numpy as np
import matplotlib.pyplot as plt


def compute_brute():
    brute100 = [14.22, 13.63, 14.06]
    brute200 = [25.72, 25.35, 25.93]
    brute300 = [45.33, 47.14, 45.10]
    brute400 = [71.73, 71.60, 72.55]
    brute500 = [106.05, 106.79, 104.64]
    brute1000 = [387.70, 419.37, 403.99]
    avg100 = np.mean(brute100)
    avg200 = np.mean(brute200)
    avg300 = np.mean(brute300)
    avg400 = np.mean(brute400)
    avg500 = np.mean(brute500)
    avg1000 = np.mean(brute1000)
    std100 = np.std(brute100)
    std200 = np.std(brute200)
    std300 = np.std(brute300)
    std400 = np.std(brute400)
    std500 = np.std(brute500)
    std1000 = np.std(brute1000)
    means = [avg100, avg200, avg300, avg400, avg500, avg1000]
    std = [std100, std200, std300, std400, std500, std1000]
    return means, std


def compute_bh05():
    bh100 = [15.91, 14.64, 15.52]
    bh200 = [21.45, 21.38, 22.65]
    bh300 = [32.14, 32.16, 29.17]
    bh400 = [37.83, 39.83, 34.91]
    bh500 = [56.95, 56.41, 46.58]
    bh1000 = [113.63, 119.97, 116.63]
    bh5000 = [732.04]
    avg100 = np.mean(bh100)
    avg200 = np.mean(bh200)
    avg300 = np.mean(bh300)
    avg400 = np.mean(bh400)
    avg500 = np.mean(bh500)
    avg1000 = np.mean(bh1000)
    avg5000 = np.mean(bh5000)
    std100 = np.std(bh100)
    std200 = np.std(bh200)
    std300 = np.std(bh300)
    std400 = np.std(bh400)
    std500 = np.std(bh500)
    std1000 = np.std(bh1000)
    std5000 = np.std(bh5000)
    means = [avg100, avg200, avg300, avg400, avg500, avg1000, avg5000]
    std = [std100, std200, std300, std400, std500, std1000, std5000]
    return means, std


def compute_bh2():
    bh100 = [12.16, 12.44, 12.02]
    bh200 = [14.40, 14.92, 14.52]
    bh300 = [19.63, 19.72, 18.70]
    bh400 = [24.45, 22.02, 21.71]
    bh500 = [25.89, 27.41, 25.28]
    bh1000 = [44.21, 46.64, 42.26]
    bh5000 = [196.50, 184.22, 190.31]
    avg100 = np.mean(bh100)
    avg200 = np.mean(bh200)
    avg300 = np.mean(bh300)
    avg400 = np.mean(bh400)
    avg500 = np.mean(bh500)
    avg1000 = np.mean(bh1000)
    avg5000 = np.mean(bh5000)
    std100 = np.std(bh100)
    std200 = np.std(bh200)
    std300 = np.std(bh300)
    std400 = np.std(bh400)
    std500 = np.std(bh500)
    std1000 = np.std(bh1000)
    std5000 = np.std(bh5000)
    means = [avg100, avg200, avg300, avg400, avg500, avg1000, avg5000]
    std = [std100, std200, std300, std400, std500, std1000, std5000]
    return means, std


def compute_bh4():
    bh100 = [12.43, 12.55, 12.21]
    bh200 = [14.65, 14.80, 13.97]
    bh300 = [16.13, 15.91, 16.69]
    bh400 = [22.34, 22.23, 24.62]
    bh500 = [26.82, 24.97, 22.82]
    bh1000 = [37.60, 33.66, 31.39]
    bh5000 = [129.11, 134.95, 125.76]
    avg100 = np.mean(bh100)
    avg200 = np.mean(bh200)
    avg300 = np.mean(bh300)
    avg400 = np.mean(bh400)
    avg500 = np.mean(bh500)
    avg1000 = np.mean(bh1000)
    avg5000 = np.mean(bh5000)
    std100 = np.std(bh100)
    std200 = np.std(bh200)
    std300 = np.std(bh300)
    std400 = np.std(bh400)
    std500 = np.std(bh500)
    std1000 = np.std(bh1000)
    std5000 = np.std(bh5000)
    means = [avg100, avg200, avg300, avg400, avg500, avg1000, avg5000]
    std = [std100, std200, std300, std400, std500, std1000, std5000]
    return means, std


def main():
    avg_brute, std_brute = compute_brute()
    avg_bh05, std_bh05 = compute_bh05()
    avg_bh2, std_bh2 = compute_bh2()
    avg_bh4, std_bh4 = compute_bh4()
    print("Brute: {}".format(avg_brute))
    print("Brute std: {}".format(std_brute))
    print("\n")
    print("BH_05: {}".format(avg_bh05))
    print("BH_05 std: {}".format(std_bh05))
    print("\n")
    print("BH_2: {}".format(avg_bh2))
    print("BH_2 std: {}".format(std_bh2))
    print("\n")
    print("BH_4: {}".format(avg_bh4))
    print("BH_4 std: {}".format(std_bh4))
    Ns = [100, 200, 300, 400, 500, 1000, 5000]
    Ns_brute = Ns[:-1]
    Ns_labels = ['100', '200', '300', '400', '500', '1000', '5000']

    fig, ax = plt.subplots(figsize=(7, 7))
    # plt.plot(Ns_brute, avg_brute, marker='.',
    # color='blue', label='brute force')
    ax.errorbar(Ns_brute, avg_brute, marker='.', ms=5, yerr=std_brute,
                color='blue', label='Brute force')
    # ax.plot(Ns, avg_bh05, marker='.', color='red', label='BH (r=0.5)')
    ax.errorbar(Ns, avg_bh05, marker='.', ms=5, yerr=std_bh05,
                color='red', label='BH (r=0.5)')
    # ax.plot(Ns, avg_bh2, marker='.', color='green', label='BH (r=2)')
    ax.errorbar(Ns, avg_bh2, marker='.', ms=5, yerr=std_bh2,
                color='green', label='BH (r=2)')
    # ax.plot(Ns, avg_bh4, marker='.', color='black', label='BH (r=4)')
    ax.errorbar(Ns, avg_bh4, marker='.', ms=5, yerr=std_bh4,
                color='black', label="BH (r=4)")
    ax.legend()
    ax.set_title('N-Body simulation time complexity')
    ax.set_xlabel('Number of bodies N')
    ax.set_ylabel('Simulation runtime (s)')
    ax.set(xlim=[90, 550], ylim=[0, 200])
    plt.show()
    fig.savefig('results_cropped.png')


if __name__ == "__main__":
    main()
