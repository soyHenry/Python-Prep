import unittest
import checkpoint as ch

class HenryChallenge(unittest.TestCase):
    
    def test_ListaEnteros(self):
      lista_test = ch.ListaEnteros(1, 10)
      lista_esperada = [1,2,3,4,5,6,7,8,9,10]
      self.assertEqual(lista_test, lista_esperada)

unittest.main(argv=[''], verbosity=2, exit=False)