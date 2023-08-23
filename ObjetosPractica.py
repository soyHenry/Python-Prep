from os import path


class Auto:
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.velocidad_actual = 0

    def acelerar(self, velocidad):
        self.velocidad_actual += velocidad
    def frenar(self, velocidad):
        self.velocidad_actual -= velocidad
    def obtener_velocidad_actual(self):
        return self.velocidad_actual
    
mi_auto = Auto('bmw', '325i', '1993', 'gris')

mi_auto.acelerar(15)

mi_auto.obtener_velocidad_actual()

sys path
