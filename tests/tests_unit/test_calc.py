import os, sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.Calc import Calc

# Fichier de description des tests au format pytest pour la classe Calc
class TestSomme(unittest.TestCase):
    def test_somme(self):
    # test de la fonction somme 
        calc = Calc()
        calcul=calc.somme([1,2,3])
        attendu=6
        self.assertEqual(calcul,attendu)

    def test_somme_erreur(self):
    # test de la fonction somme 
        calc = Calc()
        calcul=calc.somme([1,2,2])
        attendu=6
        self.assertNotEqual(calcul,attendu)

if __name__ == "__main__":
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    unittest.main()