import unittest
import os
import checkpoint as ch

class HenryChallenge(unittest.TestCase):
    
    def test_ListaEnteros_01(self):
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

    def test_DividirDosNumeros_01(self):
      parte_entera, resto = ch.DividirDosNumeros(10, 5)
      lista_test = [parte_entera, resto]
      lista_esperada = [2,0]
      self.assertEqual(lista_test, lista_esperada)

    def test_DividirDosNumeros_02(self):
      parte_entera, resto = ch.DividirDosNumeros(17, 3)
      lista_test = [parte_entera, resto]
      lista_esperada = [5,2]
      self.assertEqual(lista_test, lista_esperada)

    def test_DividirDosNumeros_03(self):
      parte_entera, resto = ch.DividirDosNumeros(13, 3)
      lista_test = [parte_entera, resto]
      lista_esperada = [4,1]
      self.assertEqual(lista_test, lista_esperada)

    def test_NumeroCapicua_01(self):
      valor_test = ch.NumeroCapicua(4589)
      valor_esperado = False
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroCapicua_02(self):
      valor_test = ch.NumeroCapicua(92529)
      valor_esperado = True
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroCapicua_03(self):
      valor_test = ch.NumeroCapicua('hola')
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroCapicua_04(self):
      valor_test = ch.NumeroCapicua(3333)
      valor_esperado = True
      self.assertEqual(valor_test, valor_esperado)

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

    def test_Factorial_03(self):
      valor_test = ch.Factorial(10)
      valor_esperado = 3628800
      self.assertEqual(valor_test, valor_esperado)

    def test_ProximoPrimo_01(self):
      valor_test = ch.ProximoPrimo(5)
      valor_esperado = 7
      self.assertEqual(valor_test, valor_esperado)
      
    def test_ProximoPrimo_02(self):
      valor_test = ch.ProximoPrimo(61)
      valor_esperado = 67
      self.assertEqual(valor_test, valor_esperado)

    def test_ProximoPrimo_03(self):
      valor_test = ch.ProximoPrimo(139)
      valor_esperado = 149
      self.assertEqual(valor_test, valor_esperado)

    def test_ProximoPrimo_04(self):
      valor_test = ch.ProximoPrimo(200)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_factorizar_numero_01(self):
      valor_test = ch.factorizar_numero(5)
      valor_esperado = [[5],[1]]
      self.assertEqual(valor_test, valor_esperado)

    def test_factorizar_numero_02(self):
      valor_test = ch.factorizar_numero(1428)
      valor_esperado = [[2,3,7,17], [2,1,1,1]]
      self.assertEqual(valor_test, valor_esperado)

    def test_factorizar_numero_01(self):
      valor_test = ch.factorizar_numero('cinco')
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

    def test_NumeroBinario_01(self):
      valor_test = ch.NumeroBinario(5)
      valor_esperado = 101
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroBinario_02(self):
      valor_test = ch.NumeroBinario(255)
      valor_esperado = 11111111
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroBinario_03(self):
      valor_test = ch.NumeroBinario(-10)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)
archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Total_Tests,Total_Fallas,Total_Errores\n')
archivo_test.write(str(resultado_test.result.testsRun)+','+str(len(resultado_test.result.failures))+','+str(len(resultado_test.result.errors))+'\n')
archivo_test.close()
print('Resumen')
print('Total Tests:', str(resultado_test.result.testsRun))
print('Total Fallas:', str(len(resultado_test.result.failures)))
print('Total Errores:', str(len(resultado_test.result.errors)))