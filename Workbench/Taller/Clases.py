class Car1:
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
        self.ruedas = 4
        self.direccion = 90
    def Acelera(self):
        self.acelera = self.aceleracion + self.velocidad
    def frena(self):
        v.frena = self.aceleracion - self.velocidad
        if v < 0:
            v = 0
        self.velocidad = 0
   

class Perro ():
    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

c1 = Car1('rojo', 20)
print (c1.color)
# rojo
print (c1.ruedas)
# 4
c2 = Car1('azul', 30)
print(c2.color)
# azul
print(c2.ruedas)
# 4