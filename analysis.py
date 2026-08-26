import numpy as np
from .lattice import vector_lengths

def _as_matrix(matrix):
    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2:
        raise ValueError("Matrix must be 2-dimensional.")
    return matrix

def basis_quality(original, reduced):
    original_lengths = vector_lengths(_as_matrix(original))
    reduced_lengths = vector_lengths(_as_matrix(reduced))
    if len(original_lengths) == 0 or len(reduced_lengths) == 0:
        raise ValueError("Bases cannot be empty.")
    original_min = float(np.min(original_lengths))
    reduced_min = float(np.min(reduced_lengths))
    ratio = 0.0 if np.isclose(original_min, 0.0) else reduced_min / original_min
    return {
        "original_shortest": original_min,
        "reduced_shortest": reduced_min,
        "ratio": ratio,
    }

def orthogonality_defect(matrix):
    matrix = _as_matrix(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Orthogonality defect requires a square matrix.")
    determinant = abs(float(np.linalg.det(matrix)))
    if np.isclose(determinant, 0.0):
        return float("inf")
    return float(np.prod(vector_lengths(matrix))) / determinant

def hadamard_ratio(matrix):
    matrix = _as_matrix(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Hadamard ratio requires a square matrix.")
    determinant = abs(float(np.linalg.det(matrix)))
    product = float(np.prod(vector_lengths(matrix)))
    if np.isclose(product, 0.0):
        return 0.0
    return (determinant / product) ** (1.0 / matrix.shape[0])

def lattice_statistics(matrix):
    lengths = vector_lengths(_as_matrix(matrix))
    if len(lengths) == 0:
        raise ValueError("Matrix must contain vectors.")
    return {
        "minimum": float(np.min(lengths)),
        "maximum": float(np.max(lengths)),
        "mean": float(np.mean(lengths)),
        "median": float(np.median(lengths)),
        "std": float(np.std(lengths)),
    }

def analyze_basis(matrix):
    matrix = _as_matrix(matrix)
    square = matrix.shape[0] == matrix.shape[1]
    determinant = float(np.linalg.det(matrix)) if square else None
    return {
        "dimension": matrix.shape,
        "rank": int(np.linalg.matrix_rank(matrix)),
        "determinant": determinant,
        "volume": abs(determinant) if determinant is not None else None,
        "condition_number": float(np.linalg.cond(matrix)),
        "orthogonality_defect": orthogonality_defect(matrix) if square else None,
        "hadamard_ratio": hadamard_ratio(matrix) if square else None,
        "statistics": lattice_statistics(matrix),
    }

def singular_values(matrix):
    return np.linalg.svd(_as_matrix(matrix), compute_uv=False)

def eigen_analysis(matrix):
    matrix = _as_matrix(matrix)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Eigenvalue analysis requires a square matrix.")
    return np.linalg.eig(matrix)

def pseudoinverse(matrix):
    return np.linalg.pinv(_as_matrix(matrix))
