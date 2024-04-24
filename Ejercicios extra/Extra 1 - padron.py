padron_alumnos = []

def agregar_alumno(nombre, apellido, edad, grado):
    alumno = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'grado': grado,
    }
    padron_alumnos.append(alumno)

while True:
    print("Ingresar los datos del alumno:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    grado = input("Grado: ")

    agregar_alumno(nombre, apellido, edad, grado)
    print(padron_alumnos)

    continuar = input("¿Desea continuar? (s/n): ")
    if continuar.lower() != "s":
        break