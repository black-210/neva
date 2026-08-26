import numpy as np

def _as_matrix(matrix):
    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2:
        raise ValueError("Matrix must be 2-dimensional.")
    return matrix

def vector_lengths(matrix):
    return np.linalg.norm(_as_matrix(matrix), axis=1)

def dot_products(matrix):
    matrix = _as_matrix(matrix)
    return matrix @ matrix.T

def angles(matrix):
    matrix = _as_matrix(matrix)
    norms = vector_lengths(matrix)
    result = np.zeros((matrix.shape[0], matrix.shape[0]))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            denominator = norms[i] * norms[j]
            if denominator == 0:
                continue
            value = np.dot(matrix[i], matrix[j]) / denominator
            result[i, j] = np.degrees(np.arccos(np.clip(value, -1, 1)))
    return result

def projections(matrix):
    matrix = _as_matrix(matrix)
    result = np.zeros_like(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            denominator = np.dot(matrix[j], matrix[j])
            if denominator == 0:
                continue
            result[i] += (
                np.dot(matrix[i], matrix[j]) / denominator
            ) * matrix[j]
    return result

def vector_order(matrix):
    return np.argsort(vector_lengths(_as_matrix(matrix)))
