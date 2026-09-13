import numpy as np
from scipy import linalg

A = np.array([
    [4, 1, 0, 0],
    [1, 4, 1, 0],
    [0, 1, 4, 1],
    [0, 0, 1, 4]
], dtype=float)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = linalg.eig(A)

print("Matrix A:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# LU decomposition
P, L, U = linalg.lu(A)

print("\nP matrix:")
print(P)

print("\nL matrix:")
print(L)

print("\nU matrix:")
print(U)
