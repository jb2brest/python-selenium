import unittest

def somme(arg):
    resultat = 0
    for val in arg:
        resultat += val
    return resultat

class TestSomme(unittest.TestCase):
    def test_somme(self):
        calcul=somme([1,2,3])
        attendu=6
        self.assertEqual(calcul,attendu)
    def test_somme_erreur(self):
        calcul=somme([1,2,2])
        attendu=6
        self.assertNotEqual(calcul,attendu)
    def test_somme_erreur(self):
        calcul=somme([1,2,3])
        attendu=6
        self.assertNotEqual(calcul,attendu)


if __name__ == "__main__":
    unittest.main()