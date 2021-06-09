# Create a matrice with 2x2 dimension with values [4,5], [3,2]. 
# Calculate determinant of this matrix using scipy.linalg. 
# Calculate the inverse of a matrix

import numpy as np
from scipy import linalg

M = np.array([[4,5], [3,2]])
det = linalg.det(M)
print("determinant of matrix is:",det)
inverse = linalg.inv(M)
print("inverse of matrix is:", inverse)