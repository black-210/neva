# NEVA-LATTICE

Lattice analysis, linear algebra, Gram-Schmidt, and LLL reduction library.

## Install

```bash
pip install -e .
```

## Example

```python
import numpy as np
from neva import analyze_basis, lll_reduce, shortest_vector

L = np.array([
    [4, 1, 3],
    [2, 1, 1],
    [1, 0, 2],
], dtype=float)

print(analyze_basis(L))

R, stats = lll_reduce(L)
print(R)
print(stats)

v, length, index = shortest_vector(R)
print(v, length, index)
```
