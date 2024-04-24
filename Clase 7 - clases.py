class Vehiculo:
    def __init__(self, color, estado, marca, modelo):
        self.color = color
        self.__estado = estado
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"El vehículo de color {self.color} y estado {self.__estado} arrancó")

    def frenar(self):
        print(f"El vehículo de color {self.color} y estado {self.__estado} frenó")

    def estacionar(self):
        print(f"El vehículo de color {self.color} y estado {self.__estado} estacionó")

vehiculo1 = Vehiculo("rojo","activo","ford","ka")
vehiculo2 = Vehiculo("gris","inactivo","chevrolet","corsa")

# vehiculo1.arrancar()
# vehiculo2.estacionar()

# print(vehiculo1.color)
# print(vehiculo2.__estado)

class Moto(Vehiculo):
    pass

class Auto(Vehiculo):
    pass

class Bicicleta(Vehiculo):
    pass

moto = Moto("azul","activo","yamaha","modelo pepito")
print(moto.marca)
# print(moto.__estado)
moto.arrancar()