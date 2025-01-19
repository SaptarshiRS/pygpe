from functools import partial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.cm import ScalarMappable
from matplotlib.colors import ListedColormap, BoundaryNorm

def integrate_circle(N=100, r=1, seed=1, disp=False):
    rng = np.random.default_rng(seed)

    # Using uniform distribution
    x = rng.uniform(-r, r, N)
    y = rng.uniform(-r, r, N)
    rs = np.hypot(x, y)

    # Integral = Area * fraction of hits
    integral = (2 * r) ** 2 * np.count_nonzero(rs <= r) / N

    if disp:
        cs = np.where(rs > r, "red", "blue")
        
        fig = plt.figure(figsize=(6, 5))
        gs = GridSpec(1, 1, figure=fig)

        ax = fig.add_subplot(gs[0])
        ax.scatter(x=x, y=y, c=cs)
        ax.set(xlabel="x", ylabel="y", xlim=(-1, 1), ylim=(-1, 1))

        cmap = ListedColormap(["blue", "red"])
        bounds = [0, 1, 2]
        norm = BoundaryNorm(bounds, cmap.N)
        fig.colorbar(ScalarMappable(cmap=cmap, norm=norm), ax=ax)

    return abs((np.pi * r ** 2) - integral)

def err_stat(Nseeds, Ns, start=0, stop=4):
    """Return the avg & std for Nseeds with Ns different point calculations,
    spread evenly over the log scale.
    Attributes:
    -----------
    Nseeds: int
        Number of seeds to average over.
    Ns: int
        Number of different sample points in log scale.
    start: int
        Start range for sample points = 10^(start).
    stop: int
        Start range for sample points = 10^(stop).
    """
    seeds = np.arange(1, Nseeds+1)
    partial_circles = list(map(lambda x: partial(integrate_circle, 
                                                 seed=x), seeds))

    errs = np.asarray([list(map(f, Ns)) for f in partial_circles])

    means = np.mean(errs, axis=0)
    stds = np.std(errs, axis=0)
    return (means, stds)
