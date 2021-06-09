# Import the essential library scipy with i/o package and Numpy.
# Create a 4 x 4 dimensional one's array.
# Store array in test.txt file.
# Get data from test.txt file and print the output.

import numpy as np
from scipy import io as sio
array = np.ones((4, 4))
sio.savemat('test.txt', {'ar': array}) 
data = sio.loadmat('test.txt', struct_as_record=True)
print(data['ar'])
