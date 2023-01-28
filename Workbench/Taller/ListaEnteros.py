"""    def test_ListaEnteros_01(self):
      lista_test = ch.ListaEnteros(1, 10)
      lista_esperada = [1,2,3,4,5,6,7,8,9,10]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaEnteros_02(self):
      lista_test = ch.ListaEnteros(3, 7)
      lista_esperada = [3,4,5,6,7,8,9,10]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaEnteros_03(self):
      lista_test = ch.ListaEnteros(-2, 4)
      lista_esperada = [-2,-1,0,1]
      self.assertEqual(lista_test, lista_esperada)

Esta función devuelve una lista de números enteros
Recibe dos argumentos:
    inicio: Numero entero donde inicia la lista
    tamanio: Cantidad de números enteros consecutivos
    Ej:
        ListaEnteros(10,5) debe retornar [10,11,12,13,14]

"""

def ListaEnteros (inicio, tamanio):
    lista = []
    for i in range(inicio, inicio + tamanio):
        lista.append(i)
    return lista

print (ListaEnteros (10,5))
print (ListaEnteros (1,10))
print (ListaEnteros (3,7))
print (ListaEnteros (-2,4))