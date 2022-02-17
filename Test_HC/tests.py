import unittest
import os
import checkpoint as ch

class HenryChallenge(unittest.TestCase):
    
    def test_ListaEnteros(self):
      lista_test = ch.ListaEnteros(1, 10)
      lista_esperada = [1,2,3,4,5,6,7,8,9,10]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaEnteros2(self):
      lista_test = ch.ListaEnteros(1, 10)
      lista_esperada = None
      self.assertEqual(lista_test, lista_esperada)

resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)
archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Total_Tests,Total_Fallas\n')
archivo_test.write(str(resultado_test.result.testsRun)+','+str(len(resultado_test.result.failures))+'\n')
archivo_test.close()
print('Resumen')
print('Total Tests:', str(resultado_test.result.testsRun))
print('Total Fallas:', str(len(resultado_test.result.failures)))