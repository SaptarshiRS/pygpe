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
import sys; sys.path.insert(0, "..")
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
from src import fermi

es = np.linspace(-1, 1, 30)
Ts = np.linspace(0.01, 1, 30)

fermi.plot_3d_slice(es, Ts)
```

```{code-cell} ipython3

```
