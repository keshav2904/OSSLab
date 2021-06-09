# Find cubic root of 27, 64, 891 using sciPy special package.

from scipy.special import cbrt
l=[27, 64, 891]
croots=cbrt(l)
for i in range(len(l)):
    print("The cube root of",l[i],":",croots[i])