alumno1 = {"Nombre":"Juan", "Apellido":"Perez", "Edad": 20}
alumno2 = {"Nombre":"María", "Apellido":"Rodriguez", "Edad": 45}
alumno3 = {"Nombre":"Fernando", "Apellido":"Gonzalez", "Edad": 16}

# Añadir clave
alumno1["Profesion"] = "Verdulero"

# Eliminar clave-valor
del alumno2["Apellido"]

# Sobreescribir el valor
alumno3["Edad"] = 18

print(alumno1)
print(alumno2)
print(alumno3)