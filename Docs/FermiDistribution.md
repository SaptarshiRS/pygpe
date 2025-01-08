---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.6
kernelspec:
  display_name: pygpe
  language: python
  name: pygpe
---

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.tri import Triangulation
from mpl_toolkits.mplot3d import Axes3D
```

## Fermi Dirac distribution

+++

The probability that a single particle, in a non-interacting Fermi gas with chemical potential $\mu$ in equilibrium at a temperature T, has energy $\epsilon$ is given by
\begin{equation}
    f_F(\epsilon) = \frac{1}{\exp{[(\epsilon - \mu)/(k_B T)]} + 1}.
\end{equation}
For particles that obey the Bose-Einstein distribution, the probability is
\begin{equation}
    f_B(\epsilon) = \frac{1}{\exp{[(\epsilon - \mu)/(k_B T)]} - 1}.
\end{equation}
Classical particles which are indistinguishable, non-interacting, non-relativistic and in thermal equilibrium, follow the Maxwell-Boltzmann distribution
\begin{equation}
    f_M(\epsilon) = \frac{1}{\exp{[(\epsilon - \mu)/(k_B T)]}}.
\end{equation}

```{code-cell} ipython3
def fermi(e, T, mu=0.1, kB=1):
    return 1 / (np.exp((e - mu) / (kB * T)) + 1)

def bose(e, T, mu=0.1, kB=1):
    return 1 / (np.exp((e - mu) / (kB * T)) - 1)
 
def maxwell(e, T, mu=0.1, kB=1):
    return 1 / (np.exp((e - mu) / (kB * T)))
 
e_ = np.linspace(-1, 1, 50)
T_ = np.linspace(0.01, 1, 50)
e, T = np.meshgrid(e_, T_)
T2d = 0.01
 
tri = Triangulation(e.ravel(), T.ravel())

fig = plt.figure(figsize=(18, 10))
gs = GridSpec(2, 3, figure=fig)

# Fermions
fT = fermi(e=e_, T=T2d)
ax = fig.add_subplot(gs[0, 0])
ax.plot(e_, fT)

ax.set_title('Fermi-Dirac Distribution function', fontsize=14)
ax.set_xlabel(r'$\epsilon$', fontsize=12)
ax.set_ylabel('f', fontsize=12)

Z = fermi(e, T)
ax = fig.add_subplot(gs[1, 0], projection='3d')
ax.plot_trisurf(tri, Z.ravel(), cmap='autumn', edgecolor='none')
 
ax.set_title('Fermi-Dirac Distribution function', fontsize=14)
ax.set_xlabel(r'$\epsilon$', fontsize=12)
ax.set_ylabel('T', fontsize=12)
ax.set_zlabel('f', fontsize=12)

# Bosons
bT = bose(e=e_, T=T2d)
ax = fig.add_subplot(gs[0, 1])
ax.plot(e_, bT)

ax.set_title('Bose-Einstein Distribution function', fontsize=14)
ax.set_xlabel(r'$\epsilon$', fontsize=12)
ax.set_ylabel('f', fontsize=12)

Z = bose(e, T)
ax = fig.add_subplot(gs[1, 1], projection='3d')

ax.plot_trisurf(tri, Z.ravel(), cmap='autumn', edgecolor='none')
 
ax.set_title('Bose-Einstein Distribution function', fontsize=14)
ax.set_xlabel(r'$\epsilon$', fontsize=12)
ax.set_ylabel('T', fontsize=12)
ax.set_zlabel('f', fontsize=12)
 
# Maxwell
mT = maxwell(e=e_, T=T2d)
ax = fig.add_subplot(gs[0, 2])
ax.plot(e_, mT)

ax.set_title('Maxwell-Boltzmann Distribution function', fontsize=14)
ax.set_xlabel(r'$\epsilon$', fontsize=12)
ax.set_ylabel('f', fontsize=12)

Z = maxwell(e, T)
ax = fig.add_subplot(gs[1, 2], projection='3d')

ax.plot_trisurf(tri, Z.ravel(), cmap='autumn', edgecolor='none')
 
ax.set_title('Maxwell-Boltzmann Distribution function', fontsize=14)
ax.set_xlabel(r'$\epsilon$', fontsize=12)
ax.set_ylabel('T', fontsize=12)
ax.set_zlabel('f', fontsize=12)
 
plt.show()
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
