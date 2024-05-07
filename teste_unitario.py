def soma(a,b):
    return a+b

def sub(a,b):
    return a - b

import unittest

class TesteUnitario(unittest.TestCase):
    def teste_soma(self):
        self.assertEqual(soma(25,15), 40)

    def teste_sub(self):
        self.assertEqual(sub(30,15), 15)

unittest.main()
