import numpy as np
import matplotlib.pyplot as plt
from math import cos, pi
if __name__ == '__main__':
    import sys

def get_seqs(fx, fy, ax, ay, phi, dt, n):
    seqs = [[], [], []]
    for i in range(n+1):
        t = dt * i
        x = ax * cos(2*pi*fx*t)
        y = ay * sin(2*pi*fy*t + phi)
        z = x + y
        seqs[0].append(str(x))
        seqs[1].append(str(y))
        seqs[2].append(str(z))
    with open("seq_output.txt", "w") as f:
        for seq in seqs:
            f.write(", ".join(seq)+"\n")
    f.close()

def get_seqs_np(fx, fy, ax, ay, phi, dt, n):
    times = np.linspace(0, n*dt, n+1)
    x = ax * np.cos(2*np.pi*fx*times)
    y = ay * np.sin(2*np.pi*fy*times + phi)
    z = x + y
    with open("seq_output2.txt", "w") as f:
        for item in [x, y, z]:
            item = item.astype('str').tolist()
            f.write(", ".join(item)+"\n")
    f.close()

def plot_seqs(fx=0, fy=0, ax=0, ay=0, phi=0, dt=0, n=0, plotz=0):
    get_seqs_np(fx, fy, ax, ay, phi, dt, n)
    seqs = []
    with open ("seq_output2.txt", "r") as f:
        for line in f:
            line = line.strip('\n')
            line = line.split(', ')
            for i in range(len(line)):
                line[i] = float(line[i])
            seqs.append(line)
    f.close()
    if plotz == 1:
        times = np.linspace(0, n*dt, n+1)
        z = seqs[2]
        plt.plot(times, z)
    else:
        x = seqs[0]
        y = seqs[1]
        plt.plot(x, y)
    plt.savefig("a1img"+name+".png", dpi=500)

fx, fy, ax, ay, phi, dt, n, plotz, name = sys.argv[1:]
fx, fy, ax, ay, phi, dt, n, plotz = float(fx), float(fy), float(ax), \
    float(ay), float(phi), float(dt), float(n), int(plotz)
plot_seqs(fx, fy, ax, ay, phi, dt, n, plotz)
