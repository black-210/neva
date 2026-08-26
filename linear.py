import numpy as np

def _as_matrix(matrix):
    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2:
        raise ValueError("Matrix must be 2-dimensional.")
    return matrix

def cross_products(matrix):
    matrix = _as_matrix(matrix)
    if matrix.shape[1] != 3:
        raise ValueError("Cross products require 3-dimensional vectors.")
    return {
        (i, j): np.cross(matrix[i], matrix[j])
        for i in range(matrix.shape[0])
        for j in range(matrix.shape[0])
    }

def determinant(matrix):
    matrix = _as_matrix(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Determinant requires a square matrix.")
    return float(np.linalg.det(matrix))

def matrix_rank(matrix):
    return int(np.linalg.matrix_rank(_as_matrix(matrix)))

def condition_number(matrix):
    return float(np.linalg.cond(_as_matrix(matrix)))
