import numpy as np
from read_numpy import T

print(np.nanmin(T))  # wartosc minimalna
print(np.nanmax(T))  # wartosc maksymalna
print(np.nanmean(T)) # wartosc srednia

# maska_bad oznacza wartosci ponizej -30 i powyzej 50
mask_bad = (T < -30) | (T > 50)

# sumujemy liczbe wartosci ponizej -30 i powyzej 50
print(mask_bad.sum())