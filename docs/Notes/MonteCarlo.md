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
from ipywidgets import interact, IntSlider
%load_ext autoreload
```

# Monte Carlo demonstration

```{code-cell} ipython3
%autoreload
from monte import integrate_circle

def f(N):
    integrate_circle(seed=1, disp=True, N=N)

interact(f, N=IntSlider(min=1, max=1000, step=10, value=10))
```

```{code-cell} ipython3
Ns = np.logspace(start=0, stop=6, base=10, num=100, dtype=np.int64)
ys = list(map(integrate_circle, Ns))

fig, ax = plt.subplots(1, 1, figsize=(5, 5))
ax.loglog(Ns, ys)
ax.set(xlabel="Samples", ylabel="Error")
```

```{code-cell} ipython3

```
