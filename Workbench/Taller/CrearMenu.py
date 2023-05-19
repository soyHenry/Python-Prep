
"""
def accion1():
    print('Has elegido la opción 1')


def accion2():
    print('Has elegido la opción 2')


def accion3():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')

#Guardamos en en un diccionario de tuplas, la opción y la acción
opciones = {
    '1': ('Opción 1', accion1),
    '2': ('Opción 2', accion2),
    '3': ('Opción 3', accion3),
    '4': ('Salir', salir)
}

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def menu_principal():
    opciones = {
        '1': ('Opción 1', accion1),
        '2': ('Opción 2', accion2),
        '3': ('Opción 3', accion3),
        '4': ('Salir', salir)
    }
generar_menu(opciones, '4')"""

# Creamos funciones asociadas a cada acción del menú
# Tercer paso es unir la lógica y para ellos crearemos con tres objetivos:
# 1) Mostrar el menú al usuario
# 2) Pedir una opción al usuario y leer esa opción por teclado.
# 3) Ejecutar la opción correspondiente.

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('Opción 1', accion1),
        '2': ('Opción 2', accion2),
        '3': ('Opción 3', accion3),
        '4': ('Salir', salir)
    }
    generar_menu(opciones, '4')

def accion1():
    print('Has elegido la opción 1')

def accion2():
    print('Has elegido la opción 2')

def accion3():
    print('Has elegido la opción 3')

def salir():
    print('Saliendo')

if __name__ == '__main__':
    menu_principal()