import numpy as np

def _as_basis(matrix):
    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2:
        raise ValueError("Basis must be a 2D matrix.")
    return matrix

def gram_schmidt(matrix):
    matrix = _as_basis(matrix)
    n = matrix.shape[0]
    G = np.zeros_like(matrix)
    mu = np.zeros((n, n), dtype=float)

    for i in range(n):
        G[i] = matrix[i]
        for j in range(i):
            denominator = np.dot(G[j], G[j])
            if np.isclose(denominator, 0.0):
                continue
            mu[i, j] = np.dot(matrix[i], G[j]) / denominator
            G[i] -= mu[i, j] * G[j]
    return G, mu

def lll_reduce(matrix, delta=0.75, max_iterations=100000):
    B = np.array(_as_basis(matrix), dtype=float, copy=True)

    if B.shape[0] == 0:
        return B, {"swaps": 0, "reductions": 0, "iterations": 0}

    if not 0.25 < delta < 1.0:
        raise ValueError("delta must satisfy 0.25 < delta < 1.0.")
    if max_iterations <= 0:
        raise ValueError("max_iterations must be positive.")

    swaps = reductions = iterations = 0
    k = 1

    while k < B.shape[0]:
        iterations += 1
        if iterations > max_iterations:
            break

        G, mu = gram_schmidt(B)

        for j in range(k - 1, -1, -1):
            q = int(np.round(mu[k, j]))
            if q:
                B[k] -= q * B[j]
                reductions += 1
                G, mu = gram_schmidt(B)

        denominator = np.dot(G[k - 1], G[k - 1])
        if np.isclose(denominator, 0.0):
            k += 1
            continue

        lhs = np.dot(G[k], G[k])
        rhs = (delta - mu[k, k - 1] ** 2) * denominator

        if lhs >= rhs:
            k += 1
        else:
            B[[k, k - 1]] = B[[k - 1, k]]
            swaps += 1
            k = max(k - 1, 1)

    return B, {
        "swaps": swaps,
        "reductions": reductions,
        "iterations": iterations,
    }

def shortest_vector(matrix):
    matrix = _as_basis(matrix)
    lengths = np.linalg.norm(matrix, axis=1)
    if len(lengths) == 0:
        raise ValueError("Basis must contain at least one vector.")
    index = int(np.argmin(lengths))
    return matrix[index].copy(), float(lengths[index]), index
