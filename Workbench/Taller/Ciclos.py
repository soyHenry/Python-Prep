print ("Inicio de números pares")
lista_p=[]                             # Creo lista pares, para poder imprimirlos hor.
lista_i=[]                             # Creo lista impares, para poder imprmirlos ver.
for par in range(0, 21, 2):            # En el rango 0-20, cada 2, partiendo de 0
    lista_p.append(par)
    print (par)
print(lista_p)                         # Escribe la lista vertical
print ("Fin de números pares")         # Escribe la lista horizontal
print ("Inicio de números impares")
for impar in range(1, 21, 2):          # En el rango 1-20, cada 2, partiendo de 1
    lista_i.append(impar)
    print (impar)                      # Escrbe la lista vertical
                                       # Escribe la lista horizontal
print(lista_i)
print ("Fin de números impares")
"""
"""# Dado un valor entero, ejecutar el mismo número de ciclos con un while
a= 5
num=1
while num < a+1:
    #print ("a vale ", a)
    #print ("num vale ", num)
    print ("Este es el ciclo", num)
    num=num+1
    

