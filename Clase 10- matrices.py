import numpy as np

# Arrays unidimensionales
a = np.array([[1,2,3,4,5,6,7,8,9,10]])
c = np.array([[2,3,6,7,3,7]])
d = np.array([[9,2,5,1,8,0]])

# Arrays bidimensionales
b = np.array([[1,8,3],[4,5,3],[7,2,9]]) #3x3
b_random = np.random.rand(3,3) #3x3

g = np.array([[4,5],[8,1],[8,2]]) #3x2
e = np.array([[3,4],[8,6]]) #2x2
f = np.array([[2,4],[7,0]]) #2x2

# Operaciones entre dos arrays unidimensionales
suma = c + d
print("Suma: ", suma)

print("Resta:")
print(c - d)

producto = c * d
print(f"Producto: {producto}")

cociente = d / c
print(f"Cociente: {cociente}")

resto = d % c
print(f"Resto: {resto}")

potencia = d ** c
print(f"Potencia entre dos arrays: {potencia}")

potencia_2 = d ** 2
print(f"Potencia al cuadrado de d: {potencia_2}")

# Operaciones entre dos arrays de diferentes dimensiones
#potencia_dif = g ** d
#print(f"Potencia entre arrays de diferentes dimensiones: {potencia_dif}")

# Multiplicación entre dos matrices bidimensionales
mult_bidim = e * f
print("Multiplicación bidimensional: ", mult_bidim)

# TODO: Utilizar las funciones: sin, cos y exp con los arrays anteriores.
# TODO: Experimentar con diferentes tamaños, formas y tipos de datos entre las operaciones ya realizadas.

# Ejercicios entre escalares
vector = np.array([[2,1,4,6,3]])
matriz = np.random.randint(1, 11, size=(3, 3)) #3x3 del 1 al 10 inclusive
escalar = 3

#TODO: Realizar la suma, resta, producto, división y potencia entre el vector y el escalar.

# Operaciones matriciales: producto punto y cruzado
producto_punto = np.dot(matriz, vector)
print(f"Producto punto: {producto_punto}")

producto_cruzado = np.cross(matriz, vector)
print(f"Producto cruzado: {producto_cruzado}")

# ¿Pudiste realizar los productos anteriores?