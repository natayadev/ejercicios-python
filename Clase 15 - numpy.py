import numpy as np

# arrange() del 0 al 10
array_arrange = np.arange(2,11,2)
print(array_arrange)

# arrange() con ceros
array_zeros = np.zeros(5)
print(array_zeros)

# arrange() con unos
array_ones = np.ones(5)
print(array_ones)

# funciones matematicas
array_trig = np.sin(array_arrange)
print(array_trig)

array_exp = np.exp(array_arrange)
print(array_exp)

array_log = np.log(array_arrange)
print(array_log)

# operaciones matematicas
array_suma = array_zeros + array_ones
print(array_suma)

array_resta = array_zeros - array_ones
print(array_resta)