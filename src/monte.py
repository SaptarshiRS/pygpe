import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.colors import ListedColormap

def integrate_circle(N=100, r=1, seed=1, disp=False):
    rng = np.random.default_rng(seed)

    # Using uniform distribution
    x = rng.uniform(-r, r, N)
    y = rng.uniform(-r, r, N)

    # Integral = Area * fraction of hits
    integral = (2*r)**2 * np.count_nonzero(np.hypot(x, y) <= r) / N

    if disp:
        fig = plt.figure(figsize=(4, 4))
        gs = GridSpec(1, 1, figure=fig)
        cmap = ListedColormap("red", "blue")

        ax = fig.add_subplot(gs[0])
        ax.scatter(x, y)
        
    return abs((np.pi * r ** 2) - integral)
