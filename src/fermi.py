import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.tri import Triangulation
from mpl_toolkits.mplot3d import Axes3D

def fermi(e, T, mu=0.1, kB=1):
    return 1 / (np.exp((e - mu) / (kB * T)) + 1)

def bose(e, T, mu=0.1, kB=1):
    return 1 / (np.exp((e - mu) / (kB * T)) - 1)
 
def maxwell(e, T, mu=0.1, kB=1):
    return 1 / (np.exp((e - mu) / (kB * T)))

def plot_3d_slice(es, Ts, T2d=0.01, mu=0.1, kB=1):
    fig = plt.figure(figsize=(18, 10))
    gs = GridSpec(2, 3, figure=fig)
    cmap = "autumn"
    edgecolor = "none"
    e, T = np.meshgrid(es, Ts)
    tri = Triangulation(e.ravel(), T.ravel())

    # Fermions
    fT = fermi(e=es, T=T2d)
    ax = fig.add_subplot(gs[0, 0])
    ax.plot(es, fT)

    ax.set_title("Fermi-Dirac Distribution function", fontsize=14)
    ax.set_xlabel(r"$\epsilon$", fontsize=12)
    ax.set_ylabel("f", fontsize=12)

    Z = fermi(e, T, mu, kB)
    ax = fig.add_subplot(gs[1, 0], projection="3d")
    ax.plot_trisurf(tri, Z.ravel(), cmap=cmap, edgecolor=edgecolor)
     
    ax.set_title("Fermi-Dirac Distribution function", fontsize=14)
    ax.set_xlabel(r"$\epsilon$", fontsize=12)
    ax.set_ylabel("T", fontsize=12)
    ax.set_zlabel("f", fontsize=12)

    # Bosons
    bT = bose(e=es, T=T2d)
    ax = fig.add_subplot(gs[0, 1])
    ax.plot(es, bT)

    ax.set_title("Bose-Einstein Distribution function", fontsize=14)
    ax.set_xlabel(r"$\epsilon$", fontsize=12)
    ax.set_ylabel("f", fontsize=12)

    Z = bose(e, T, mu, kB)
    ax = fig.add_subplot(gs[1, 1], projection="3d")

    ax.plot_trisurf(tri, Z.ravel(), cmap=cmap, edgecolor=edgecolor)
     
    ax.set_title("Bose-Einstein Distribution function", fontsize=14)
    ax.set_xlabel(r"$\epsilon$", fontsize=12)
    ax.set_ylabel("T", fontsize=12)
    ax.set_zlabel("f", fontsize=12)
     
    # Maxwell
    mT = maxwell(e=es, T=T2d)
    ax = fig.add_subplot(gs[0, 2])
    ax.plot(es, mT)

    ax.set_title("Maxwell-Boltzmann Distribution function", fontsize=14)
    ax.set_xlabel(r"$\epsilon$", fontsize=12)
    ax.set_ylabel("f", fontsize=12)

    Z = maxwell(e, T, mu, kB)
    ax = fig.add_subplot(gs[1, 2], projection="3d")

    ax.plot_trisurf(tri, Z.ravel(), cmap=cmap, edgecolor=edgecolor)
     
    ax.set_title("Maxwell-Boltzmann Distribution function", fontsize=14)
    ax.set_xlabel(r"$\epsilon$", fontsize=12)
    ax.set_ylabel("T", fontsize=12)
    ax.set_zlabel("f", fontsize=12)
     
    plt.show()
