import numpy as np

A = np.array([1, 2, 3, 4, 5]).shape
B = np.array([1, 2, 3, 4, 5]).dtype
C = np.array([1, 2, 3, 4, 5])[0]
D = len(np.array([1, 2, 3, 4, 5]))

print(A, B, C, D)
print(np.array([1, 2, 3, 4, 5]).ndim)
print(np.array([1, 2, 3, 4, 5]).size)
print(np.array([1, 2, 3, 4, 5]).itemsize)
print(np.array([1, 2, 3, 4, 5]).data)
print(np.array([1, 2, 3, 4, 5]).tobytes())
print(np.array([1, 2, 3, 4, 5]).tolist())
print(np.array([1, 2, 3, 4, 5]).reshape(5, 1))
print(np.array([1, 2, 3, 4, 5]).reshape(1, 5))

v1 = np.array([1, 2, 3, 4, 5])
v2 = np.array([5, 4, 3, 2, 1])

print(np.add(v1, v2))
print(np.lib.scimath.sqrt(-1))
print(np.linalg.norm(v1))
print(np.linalg.norm(v2))

np.zeros((3, 3))
np.eye(3)
np.dot(v1, v2)

print("\nNEVA-LATTICE")

n = int(input("Dimension: "))

rows = []

for i in range(n):
    row = list(map(float, input(f"Row {i + 1}: ").split()))

    if len(row) != n:
        print(f"Row must contain {n} values")
        exit()

    rows.append(row)

L = np.array(rows)

print("\nLattice")
print(L)

print("\nElements")

for i in range(n):
    for j in range(n):
        print(f"L[{i}][{j}] = {L[i][j]}")

print("\nDeterminant")
print(np.linalg.det(L))

print("\nVector norms")

for i in range(n):
    print(f"Norm of row {i + 1}: {np.linalg.norm(L[i])}")

print("\nDot products")

for i in range(n):
    for j in range(n):
        print(
            f"Dot product {i + 1},{j + 1}: "
            f"{np.dot(L[i], L[j])}"
        )

print("\nAngles")

for i in range(n):
    for j in range(n):
        denominator = (
            np.linalg.norm(L[i]) *
            np.linalg.norm(L[j])
        )

        if denominator == 0:
            angle = 0
        else:
            value = np.dot(L[i], L[j]) / denominator
            value = np.clip(value, -1.0, 1.0)
            angle = np.degrees(np.arccos(value))

        print(
            f"Angle {i + 1},{j + 1}: "
            f"{angle} degrees"
        )

print("\nProjections")

for i in range(n):
    for j in range(n):

        denominator = np.dot(L[j], L[j])

        if denominator == 0:
            projection = np.zeros(n)
        else:
            projection = (
                np.dot(L[i], L[j])
                / denominator
                * L[j]
            )

        print(
            f"Projection {i + 1} -> {j + 1}: "
            f"{projection}"
        )

print("\nGram-Schmidt")

G = np.zeros((n, n))

for i in range(n):
    for j in range(n):

        denominator = np.dot(L[j], L[j])

        if denominator != 0:
            G[i][j] = (
                np.dot(L[i], L[j])
                / denominator
            )

        print(f"G[{i}][{j}] = {G[i][j]}")

print("\nEigenvalues")
print(np.linalg.eigvals(L))

print("\nEigenvectors")
print(np.linalg.eig(L)[1])

print("\nSingular Values")
print(np.linalg.svd(L)[1])

if n == 3:

    print("\nCross Products")

    for i in range(n):
        for j in range(n):
            print(
                f"Cross {i + 1},{j + 1}: "
                f"{np.cross(L[i], L[j])}"
            )

print("\nLLL Reduction")

delta = 0.75
R = L.copy()
k = 1

while k < n:

    for j in range(k - 1, -1, -1):

        denominator = np.dot(R[j], R[j])

        if denominator == 0:
            continue

        mu = np.dot(R[k], R[j]) / denominator

        if abs(mu) > 0.5:
            R[k] = R[k] - round(mu) * R[j]

    denominator = np.dot(R[k - 1], R[k - 1])

    if denominator == 0:
        k += 1
        continue

    mu = (
        np.dot(R[k], R[k - 1])
        / denominator
    )

    left = np.linalg.norm(R[k]) ** 2

    right = (
        delta - mu ** 2
    ) * np.linalg.norm(R[k - 1]) ** 2

    if left >= right:

        k += 1

    else:

        R[[k, k - 1]] = R[[k - 1, k]]

        k = max(k - 1, 1)

print("\nOriginal Basis")
print(L)

print("\nReduced Basis")
print(R)

print("\nOriginal Norms")

for i in range(n):
    print(
        f"Norm {i + 1}: "
        f"{np.linalg.norm(L[i])}"
    )

print("\nReduced Norms")

for i in range(n):
    print(
        f"Norm {i + 1}: "
        f"{np.linalg.norm(R[i])}"
    )

print("\nReduction Complete")
