# Plot tan(x), cot(x), sec(x) and cosec(x) for the values of x= [-pi,-pi/4, -pi/2, 0, pi/4, pi/2, pi].

import numpy as np
X = np.array([-np.pi, -np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2, np.pi])
T, C, S, CO = np.tan(X), np.arctan(X), np.arccos(X), np.arcsin(X)
import matplotlib.pyplot as plt
plt.subplot(2,2,1)
plt.plot(X, T)
plt.subplot(2,2,2)
plt.plot(X, C)
plt.subplot(2,2,3)
plt.plot(X, S)
plt.subplot(2,2,4)
plt.plot(X, CO)
plt.show()