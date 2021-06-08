# Plot tan(x), cot(x), sec(x) and cosec(x) for the values of x= [-pi,-pi/4, -pi/2, 0, pi/4, pi/2, pi].

import numpy as np
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
T, C, S, CO = np.tan(X), np.arctan(X), np.arccos(X), np.arcsin(X)
import matplotlib.pyplot as plt
plt.plot(X, T)
plt.show()
plt.plot(X, C)
plt.show()
plt.plot(X, S)
plt.show()
plt.plot(X, CO)
plt.show()