# Create Sparse matrices A and B and analyze various functions of sciPy sparse package

import numpy as np
from scipy import sparse

A = np.array([[0, 0],[0, 1],[3, 0]])
B = np.array([[0, 2, 0],[2, 0, 1],[0, 3, 0]])
matrix_sparse_A = sparse.csr_matrix(A)
matrix_sparse_B = sparse.csr_matrix(B)
print(matrix_sparse_A)
print()
print(matrix_sparse_B)
print()
print(sparse.eye(3,4))
print()
print(sparse.identity(4))
print()
print(sparse.find(B))
print(sparse.issparse(B))
print(sparse.issparse(matrix_sparse_B))