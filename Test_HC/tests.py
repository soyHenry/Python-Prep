import unittest
import os
import checkpoint_ejemplo as ch

class HenryChallenge(unittest.TestCase):
    
    def test_Func_Ejemplo_1(self):
      valor_test = ch.Func_Ejemplo(1,2)
      valor_esperado = 1
      self.assertEqual(valor_test, valor_esperado)
      
    def test_Func_Ejemplo_2(self):
      valor_test = ch.Func_Ejemplo(1,2)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)