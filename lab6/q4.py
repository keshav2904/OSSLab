# Define two-dimensional array with values {(5,4),(6,3)}.
# Output eigen values and eigenvectors of the matrix.

import numpy as np
from scipy import linalg

M = np.array([[5,4],[6,3]])
eigenvalues, eigenvectors = linalg.eig(M)
print(eigenvalues)
print(eigenvectors)