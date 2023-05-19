import unittest
import os
import checkpoint as ch

class PruebaHenryChallenge(unittest.TestCase):
    
    def test_Factorial_01(self):
      valor_test = ch.Factorial(5)
      valor_esperado = 120
      self.assertEqual(valor_test, valor_esperado)

    def test_Factorial_02(self):
      valor_test = ch.Factorial(1)
      valor_esperado = 1
      self.assertEqual(valor_test, valor_esperado)

    def test_Factorial_03(self):
      valor_test = ch.Factorial(0)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_EsPrimo_01(self):
      valor_test = ch.EsPrimo(5)
      valor_esperado = True
      self.assertEqual(valor_test, valor_esperado)
      
    def test_EsPrimo_02(self):
      valor_test = ch.EsPrimo(27)
      valor_esperado = False
      self.assertEqual(valor_test, valor_esperado)

    def test_EsPrimo_03(self):
      valor_test = ch.EsPrimo('parametro incorrecto')
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseAnimal_01(self):
      a = ch.ClaseAnimal('perro','negro')
      valor_test = a.CumplirAnios()
      valor_test = a.CumplirAnios()
      valor_test = a.CumplirAnios()
      valor_esperado = 3
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseAnimal_02(self):
      a = ch.ClaseAnimal('ballena','azul')
      for i in range(0,10):
        valor_test = a.CumplirAnios()
      valor_esperado = 10
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseAnimal_03(self):
      a = ch.ClaseAnimal('tortuga','verde')
      for i in range(0,100):
        valor_test = a.CumplirAnios()
      valor_esperado = 100
      self.assertEqual(valor_test, valor_esperado)

resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests - hc_fallas - hc_errores

archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Total_Tests,Total_Fallas,Total_Errores,Total_Correctos\n')
archivo_test.write(str(hc_tests)+','+str(hc_fallas)+','+str(hc_errores)+','+str(hc_ok)+'\n')
archivo_test.close()

print('Resumen')
print('Total Tests:', str(hc_tests))
print('Total Fallas:', str(hc_fallas))
print('Total Errores:', str(hc_errores))
print('Total Correctos:', str(hc_ok))