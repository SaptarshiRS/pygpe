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

+++

## Setup

I am demonstrating a very simple way to visualize the concept of Monte-Carlo integration. The main idea revolves around the concept that we randomly (uniform distribution) pick points in a given volume (which must include the domain of the function that we want to integrate) and decide by some parameter what fraction of the points actually contribute to the integral. For a closed function, this can be done by simply evaluating the function at the random points and checking if they are within the function boundary.
Finally, the product of the total sample space and the fraction of relevant points gives us the integral.

We know the area of a circle is $\pi r^2$, where $r$ is the radius of the circle.
Assuming unit radius, the area becomes equal to $\pi$ and is a method for finding the value of $\pi$.

The diagram below has radius set to $1$ (but I can change it, by passing the `r` parameter) and the axes represent the usual coordinate axes. I seed the `Generator` (a Numpy random number generator) and generate N floats in the range $\left(0, r\right)$ as the abscissa of the sample points, followed by another set of N points for the ordinates.

Then I calculate the hypotenuse (or the magnitude of the position vector, or the effective radius) for each point and if that falls in the range $\left(0, r\right)$ then I increment a counter by $1$ and also keep a list to denote that the point whould be colored blue.

Once all the sample points are accounted for, the final value of the counter divided by the total number of sample points gives us the ratio of the area which is useful to us (or the proability that the rangom guess falls in the region of interest). Finally, I multiply this ratio (probability) with the total area under consideration (volume of the sample space) and we get the integration result, which in our case is also the area of the circle and the value of $\pi$.

\begin{equation}
    \text{Area} = \left(2 r\right)^2 \times \frac{\text{Points at most $r$ away from origin}}{\text{Total number of points}} = \pi r^2.
\end{equation}

```{code-cell} ipython3
%autoreload
from monte import integrate_circle

def f(N): integrate_circle(seed=1, disp=True, N=N)
interact(f, N=IntSlider(min=1, max=2000, step=20, value=1000));
```

## Error scaling

The function `integrate_circle()` returns the absolute difference of $\pi r^2$ from the result that we got from the Monte-Carlo integration. The accuracy of this integration technique increases with the number of sampling points and I wanted to check how it relates to increasing the points.

So, I picked a range $\left(1, 10^6\right)$ and plotted how this error decreases with increasing number of points. It is important to note that there are local fluctuations arise from two main reasons. Firstly, because of how coarsely I binned this range. Here I am taking a total of 100 points spread logarihmically over the range and increasing the granularity would make the trend smoother. Secondly, since the points are chosen at random, sometimes the points can be clustered inside the zone of interest and vice-versa thereby causing the fluctuation.

```{code-cell} ipython3
Ns = np.logspace(start=0, stop=6, base=10, num=100, dtype=np.int64)
ys = list(map(integrate_circle, Ns))

fig, ax = plt.subplots(1, 1, figsize=(5, 5))
ax.loglog(Ns, ys)
ax.set(xlabel="Samples", ylabel="Error", title="Error scaling");
```

```{code-cell} ipython3

```
