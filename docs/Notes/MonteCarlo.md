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
%load_ext autoreload
```

# Monte Carlo demonstration

```{code-cell} ipython3
%autoreload
from monte import integrate_circle

integrate_circle(seed=1, disp=True)
```

```{code-cell} ipython3
Ns = np.logspace(start=1, stop=6, base=10, num=100, dtype=np.int64)
ys = list(map(integrate_circle, Ns))

plt.loglog(Ns, ys)
plt.xlabel("Samples")
plt.ylabel("Error")
```

```{code-cell} ipython3

```
