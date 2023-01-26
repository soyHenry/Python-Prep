
class Alumnos:

    def __init__(self):
        self.nombres=[]
        self.notas=[]

# El método menu muestra una serie de opciones y solicita al usuario que
# elija una de ellas, según cual de ellas selecciona procede a llamar al método respectivo:
    def menu(self):
        opcion=0
        while opcion!=4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.notas_altas()
# Algo que no utilizamos hasta ahora del lenguaje Python, es una forma
# simplificada de if anidados con la sentencia elif:
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.notas_altas()
# Nosotros, hasta ahora, lo resolvíamos y podemos sin problema seguir utilizando
# la sintaxis::
            if opcion==1:
                self.cargar()
            else:
                if opcion==2:
                    self.listar()
                else:
                    if opcion==3:
                        self.notas_altas()
# Pero podemos comprobar que, si hay muchos if anidados la nueva sintaxis es más
# clara.
# Un ciclo WHILE, repite el método menu, mientras no se ingrese como opción en la
# variable local, el valor 4.

# El método cargar, se llama desde el método menu, en el mismo procedemos a cargar
# las dos listas paralelas, con los nombres de alumnos y sus notas:

    def cargar(self):
        for x in range(5):
            nom=input("Ingrese nombre del alumno:")
            self.nombres.append(nom)
            no=int(input("Nota del alumno:"))
            self.notas.append(no)

# El método listar muestra las dos listas paralelas por completo e imprime una línea separadora para que se vea in forma más clara:

    def listar(self):
        print("Listado completo de alumnos")
        for x in range(5):
            print(self.nombres[x],self.notas[x])
        print("_____________________")            
# Finalmente el método notas_altas muestra solo los elementos de las listas cuyas
# notas sean igual o superior a 7:

    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7")
        for x in range(5):
            if self.notas[x]>=7:
                print(self.nombres[x],self.notas[x])
        print("_____________________")    
# bloque principal

alumnos=Alumnos()
alumnos.menu()
