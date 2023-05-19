def NumeroCapicua(numero):
    '''
    En matemáticas, la palabra capicúa (del catalán cap i cua, 'cabeza y cola')​ 
    se refiere a cualquier número que se lee igual de izquierda a derecha que 
    de derecha a izquierda. Se denominan también números palíndromos.
    Esta función devuelve el valor booleano True si el número es capicúa, de lo contrario
    devuelve el valor booleano False 
    En caso de que el parámetro no sea de tipo entero, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número sobre el que se evaluará si es capicúa o no lo es.
    Ej:
        NumeroCapicua(787) debe retornar True
        NumeroCapicua(108) debe retornar False
    '''
    cadena3 = str(numero)
    pali    = []
    pali2   = []
    if type(numero) == int:
        for i in range(len(cadena3) -1, -1, -1):
            pali.append(cadena3[i])
        for j in range(len(pali)-1, -1, -1):
            pali2.append(pali[j])
        if (pali == pali2):
            return True
        else:
            return False
    else:
        return None


# Probar
numeros = [11, 20, 123, 9889, 2811, 1801, 777, 12321, ]

for num in numeros:
    es_capicua = NumeroCapicua(num)
    print(f"El número {num} es capicúa? {es_capicua}")