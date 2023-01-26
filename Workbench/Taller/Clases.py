#*******************************************************************
#*                                                                 *
#*                     TALLLER CLASES y OBJETOS                    *
#*                                                                 *
#*******************************************************************
# En Python todo son clases, porque es un lenguaje flexible
# Una clase es la abstracción de un objeto, un molde para crear entidades similares.
# Una clase consta de ATRIBUTOS y MÉTODOS
# Con los atributos o CONSTRUCTOR se instancia (crea) el objeto, es una copia
# Con los métodos se manipula, se hacen cálculos, se accede al objeto. 
# Un ATRIBUTO es una carcterística, cuantificable o no, que define al objeto, ej, su color, número de patas
# Como ATRIBUTO, a un objeto le puedo definir cualquuier cosa ej diccionario, listas, tuplas
# Agregamos los atributos que necesitemos y si es numérico se inicializan con algún valor, ej velocidad=0.
# Los ATRIBUTOS o se deben acceder desde fuera de la clase(ej print(a1.color), a1 es un objeto animal, 
# con un atributo llamado color, en principio, la sentencia devolvería el color de a1, con el que fue
# creado, pero la buena práctica dice que debemos crear un método para acceder a su color y luego podemos
# imprimir lo que retorna el método.
# Para proteger un ATRIBUTO, se le agregan dos lineas bajas o underscore al INICIO del atributo.
# Luego creo los métodos o funciones asociados a él o los ATRIBUTOS, similar a los geters y seters.
# Este es un ejemplo de ENCAPSULACIÓN
# Un MÉTODO, básicamente, es una FUNCIóN, usada para ejecutar procedimientos u operaciones sobre la CLASE
# con los ATRIBUTOS de la CLASE. Por ejemplo, un objeto auto, tiene un atributo velocidad, por lo que puede acelerar o frenar.
# Qué es ABSTRACCIÓN => Separar los datos
# Qué es ENCAPSULAMIENTO => Proteger el objeto (lo accedo o conozco a través de sus métodos)
# Qué es HERENCIA => Permite crear nuevas clases heredando sus atributos,métodos y agregando nuevos, 
# ej. Animales=>Humano
# Qué es POLIMORFISMO => Mismo nombre pero distinto comportamiento
# Se usa la palabara reservada class, seguida de __INIT__, y detro de los paréntesis (), la primera palabra
# DEBE ser self, seguido de sus atributos. A esto se denomina el método CONSTRUCTOR de la clase.
# SELF es una palabra reservada que le dice a Python que lo que viene son atributos y no genere conflictos.
# Para que la ayuda o help(), despliegue un mensaje de qué hace una CLASE o FUNCIÓN, se abren 
# tres comillas dobles, se agrega una breve descripción con los tipos de varibles o sintaxis, y se vuelve
# a cerrar con tres comillas dobles.
# 

# Ej 1) Crear una clase que cree objetos del tipo automóvil con los atributos color y aceleración

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

# Ej 5 Crear una función que cree la clase Emprendedor
# El constructor de la clase Emprenddedor recibe los valores 
# nombre (str), apellido (str), libros (array), mascotas (array de str)
# Inicializar las propiedades de la clase Emprendedor con los valores recibidos
class Emprendedor:
    """
    recibe los valores nombre (str), apellido (str), libros (array),
    mascotas (array de str)
    """
    def __init__(self, nombre, apellido, libros, mascotas):
        self.nombre = nombre
        self. apellido = apellido   #Este es el constructor de la clase
        self.libros = libros
        self. mascotas = mascotas

# Estos los métodos de la clase Emprendedor
    def getNombre (self):           
        pass
    def getApellido (self):
        pass
    def getLibros (self):
        pass
    def getMascotas (self):
        pass
    def setNombre (self):
        pass
    def setApellido (self):
        pass
    def setLibros (self):
        pass
    def setMascotas (self):
        pass 

# Ej 6 Creamos el objeto emp1 con el constructor Emprendedor
emp1 = Emprendedor ("Lionel", "Cordova", ["Dos palmeras", 1917, 'abc123'], ('Perro', 'Gato'))
print ("")
print (type(emp1))          # Debe retornar <class '__main__.Emprendedor'>
print (type(emp1.nombre))   # Debe retornar <class 'str'>
print (type(emp1.apellido)) # Debe retornar <class 'str'>
print (type(emp1.libros))   # Debe retornar <class 'list'>
print (type(emp1.mascotas)) # Debe retornar <class 'tuple'>
print("")

# Ej 8 ENCAPSULAMIENTO
# Encapsular, consiste en hacer que los atributos o métodos internos a una clase no se puedan
# acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos.
# Python por defecto NO OCULTA los atributos y métodos de una clase al exterior.
# 
class miSaludo:
    atributo_clase = "Hola"
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia
# Mira lo que pasa
prueba_mi_clase = miSaludo("Que tal")       #Instancio el objeto con el parámetro 'Que tal'=atributo_instancia
print (prueba_mi_clase.atributo_clase)      # Le he pasado el valor de la variable
print (prueba_mi_clase.atributo_instancia)  # Le he pasado el parámetro de la instancición de la clase

# 'Hola'
# 'Que tal'

# Primera reflexión: Ambos atributos son perfectamente accesibles desde el exterior!, va contra las buenas prácticas.
# Hay métodos o atributos que queremos que pertenezcan sólo a la clase o al objeto, y que sólo puedan ser accedidos
# por los mismos. Para ello podemos usar la doble __ (underscore) para ocultar un atributo o método.
# Esto hará que Python los interprete como “privados”, y ya no podrán ser accedidos desde el exterior.
# Eso es "ENCAPSULAMIENTO"
# Volvamos a revisar el ejemplo
class Clase:
    atributo_clase = "Hola"   # Es accesible desde el exterior
    __atributo_clase = "Hola" # No es accesible desde el exterior de la clase
    # Acá protegemos el método, ahora no es accesible desde el exterior
    def __mi_metodo(self):
        print("Este es un ejemplo de ENCAPSULAMIENTO")
        self.__variable = 0   # La variable, también la hacemos privada

    # Este método lo exponemos para acceder a la clase, debe ser accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__mi_metodo()

mi_clase = Clase()
#mi_clase.__atributo_clase  # Error! El atributo no es accesible
#mi_clase.__mi_metodo()     # Error! El método no es accesible
mi_clase.atributo_clase     # Ok!
mi_clase.metodo_normal()    # Ok!
# Podemos hacer uso de 'dir' para ver el listado de métodos y atributos de nuestra clase que son PUBLICOS.
# Al hacer 'privados' el '_atributo_clase' y '_mi_metodo', no los podremos encontrar en la lista.
print(dir(mi_clase))
#['_Clase__atributo_clase', '_Clase__mi_metodo', '_Clase__variable',
#'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
#'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#'__str__', '__subclasshook__', '__weakref__', 'atributo_clase', 'metodo_normal']

# Se puede acceder a los atribtos y métodos ocultos de una clase, como  '__atributo_clase' y a '__mi_metodo',
# haciendo un poco de trampa.
# Python los guarda con un nombre distinto para ocultarlos (encapsularlos) y evitar su uso indebido.
# Podemos llamarlos con un 'truco sucio' de la siguiente manera aunque, por buenas prácticas, no es recomendable.
print("")
a = mi_clase._Clase__atributo_clase
print ("Escribiendo 'la ruta completa' del atributo oculto")
print ("de esta forma: 'mi_clase._Clase__atributo_clase', retornará su contenido")
print ("en este caso ", a)
# 'Hola'
print ("Caso 2, al escribir 'la ruta completa' del método así 'mi_clase._Clase__mi_metodo', retorna su contenido.")
print ("en este caso ", mi_clase._Clase__mi_metodo()) 
# Conclusión, hay una precedencia en las operaciones...la función primero que el
# print, y se repite porque imprime la función y lo que retorna que es none.
# Por esa razón, a veces parece que se imprime en otra parte.   


# Ej 7 POLIMORFISMO
# Suponga que tiene una clase ANIMAL, que tiene un atributo HABLAR
print("")
class Animal:         # Creamos la clase con 1 atributo hablar 
    def hablar(self):
        pass
# Por otro lado, creamos dos clases: Perro y Gato, que heredan de la anterior.
# Además, implementan el método hablar() de formas distintas.
# Entonces:
print ("")
class Perro(Animal):  # Nótese que en este caso se le pasa como parámetro, la otra
    def hablar(self): # clase entre paréntesis.
        print("Guau!")
                
class Gato(Animal):
    def hablar(self):
        print("Miau!")

# Ahora creamos un objeto de cada clase y llamamos al método hablar().
# Podemos observar que cada animal se comporta de manera distinta al usar hablar().

for sonidos in Perro(), Gato():
    sonidos.hablar()
# Guau!
# Miau!

