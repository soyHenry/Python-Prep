# Buscar una subcadena con index
import re
obj_iter="palabra"
varany  = int
pos_ini = int
pos_fin = int
# obj_iter.sub[varany, pos_ini, pos_fin]) 
# es similar a find() pero en caso de que no se encuentre la subcadena sub lanza la excepción ValueError.
# TypeError : Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado.
# ZeroDivisionError : Ocurre cuando se itenta dividir por cero.
# OverflowError : Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
# IndexError : Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
# KeyError : Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
# FileNotFoundError : Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.
# ImportError : Ocurre c
# Manejo de excepciones con TRY y EXCEPT
# try:
	# Codigo a ejecutar
	# Pero podria haber errores en este bloque
#    
# except <tipo de error>:
	# Haz esto para manejar la excepcion
	# El bloque except se ejecutara si el bloque try lanza un error
#    
# else:
	# Esto se ejecutara si el bloque try se ejecuta sin errores
#   
# finally:
	# Este bloque se ejecutara siempre
print ("")
frase = 'me gusta la mermelada'
busca = "lo"
try:
    cadena = frase
    print (cadena.index(busca))
    # La cadena 'lo' no existe, por lo que provocará un error 
except ValueError:
    print ("En el texto ", "'",cadena,"'", "no existe la cadena", busca)

# Otro ejemplo, creamos una función "dividir" que divide dos números
num = 10
div = 0
def dividir(num,div):
    try:
        res = dividir(num, div)
        print(res)
    except ZeroDivisionError:
        print("Trataste de dividir entre cero :( ")
    return num/div 
#Sin embargo no controla la división por 0, que no esta definida y devolverá un error
#Aquí usamos el control de errores con try y except

# Traceback (most recent call last):
# File "<input>", line 1, in <module>
# ValueError: substring not found

# Ejemplo
# Buscar la posición de una cadena, en el ejemplo "la"
# Debe retornar la pos anterior a dónde incia la cadena, en este caso 9
print ("La posición anterior a iniciar la primera cadena 'la' que encuentra, es la pos ", cadena.index('la')) 
print ("")

# Ejemplo
# Encontrar la última posición de una subcadena con RFIND, la busca todas y devuelve la ÚLTIMA
cadena = 'me gusta la mermelada'
cadena.rfind('la') # ocupan las pos 18 y 19
print ("La última posición anterior, a iniciar la cadena 'la', es la pos ", cadena.rfind('la'))
# 17
print (cadena.rfind('lo'))
# -1
# Encontrar la última posición de una subcadena con RINDEX
print (cadena.rindex('la'))
# 17
# print (cadena.rindex('lo'))
# Debe arrojar un error porque no existe la cadena (ValueError: substring not found)
import re
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ",  "-",  texto)
print(busqueda)