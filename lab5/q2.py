# Represent the following table using bar chart:
# Method Result1 Result2
# A 2 3
# B 5 2
# C 8 5
# D 5 7

import numpy as np
import matplotlib.pyplot as plt
n = 4
X = np.array([1,2,3,4])
Method = np.array(['A', 'B', 'C', 'D'])
R1 = np.array([2, 5, 8, 5])
R2 = np.array([3, 2, 5, 7])
plt.bar(X-0.1, R1, width=0.2, facecolor='#9999ff', edgecolor='white')
plt.bar(X+0.1, R2, width=0.2, facecolor='#ff9999', edgecolor='white')
plt.show()