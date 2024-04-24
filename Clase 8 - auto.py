class Auto:
    def __init__(self, color, peso, tamanio, alto, largo, cantidad_ruedas, cantidad_puertas, tipo):
        self.color = color
        self.peso = peso
        self.tamanio = tamanio
        self.alto = alto
        self.largo = largo
        self.cantidad_ruedas = cantidad_ruedas
        self.cantidad_puertas = cantidad_puertas
        self.tipo = tipo
        self.detenido = True
        self.circulando = False
        self.estacionado = True
        self.daniado = False

    def arrancar(self):
        print(f"Arrancando el auto color {self.color}...")
        self.detenido = False
        self.estacionado = False
        self.circulando = True
        print(f"Estado detenido: {self.detenido}")
        print(f"Estado estacionado: {self.estacionado}")

    def frenar(self):
        print("Frenando...")
        self.detenido = True

    def acelerar(self):
        print("Acelerando...")

    def girar(self):
        print("Girando...")

auto = Auto("rojo",1500,"grande",2,4,4,4,"gasolero")
auto.arrancar()
auto.girar()

class Bicicleta:
    def __init__(self, color, rodado, marca):
        self.color = color
        self.rodado = rodado
        self.marca = marca
    
    def pasear(self):
        pass

    def competir(self):
        pass

    def girar(self):
        pass