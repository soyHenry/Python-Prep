# Ejercicio 1 - Obtener la inversa de un string
# Invertir cualquier cadena de caracteres

cadena1 = "cebolla" # R=> allobec
cadena2 = "somos"  # R=> 'somos', es palíndroma

for i in range(len(cadena1) -1, -1, -1):
    print (cadena1[i], end="")

print()

# Ejercicio 2 - Palabra inversa, caso PALÍNDROMO (se lee igual al revés)
# Detectar si es palíndromo y mandar un mensaje

cadena3 = "coco" # R=> ococ
cadena4 = "reconocer"  # R=> 'reconocer', es palíndroma
pali    = []
pali2   = []
for i in range(len(cadena3) -1, -1, -1):
    pali.append(cadena3[i])
for j in range(len(pali)-1, -1, -1):
    pali2.append(pali[j])
#print (pali)  # Se puede eliminar, es sólo para controlar la salida y sirven de manejo de errores
#print (pali2) # Se puede eliminar, es sólo para controlar la salida y sirven de manejo de errores
if (pali == pali2):
    print ("Felicitaciones", cadena3, "es un palíndromo", end="")
else:
    print ("La palabra","'", cadena3,"'", "no es palíndroma e invertida, es", pali, end="")
print()

# Ejercicio 3 - Palabra inversa usando propiedades del método print - SLICING
print ('')
cadena= 'Pepino' 
print (cadena[::-1]) # '::' Indica de 0 hasta el último de los caracteres, 
                     # para variantes, funciona igual que los indices separados
                     # por ':', con un desde y hasta, finalmente el '-1', le
                     # indica al método que es en orden inverso.

# Ejercicio 4  - Ordenar una lista de cadenas de caracteres según el último carácter con la
# función sorted()
# 

# Creamos un diccionario dic_cadenas y que almacena 8 str (ciudades)
# 

dic_cadenas = ['Talca', 'París', 'Londres', 'Bogotá', 'San José', 'Santiago', 'Lima', 'Sao Paulo']
print (dic_cadenas)

print()

