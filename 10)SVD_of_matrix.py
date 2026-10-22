from numpy import matrix, matmul, diag
from scipy.linalg import svd

# Define a matrix
A = matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

print("Matrix A:\n", A)

# Singular Value Decomposition
U, S, V = svd(A)

print("\nMatrix U:\n", U)
print("\nSingular values S:\n", S)
print("\nMatrix V:\n", V)

# Create diagonal matrix
Sigma = diag(S)

print("\nDiagonal matrix Sigma:\n", Sigma)

# Reconstruct the original matrix
B = matmul(U, matmul(Sigma, V))

print("\nReconstructed Matrix B:\n", B)
