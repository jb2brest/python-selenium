import os, sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import classes.calc as Calc


class TestSomme(unittest.TestCase):
    def test_somme(self):
        calc = Calc()
        calcul=calc.somme([1,2,3])
        attendu=6
        self.assertEqual(calcul,attendu)

    def test_somme_erreur(self):
        calc = Calc()
        calcul=calc.somme([1,2,2])
        attendu=6
        self.assertNotEqual(calcul,attendu)

if __name__ == "__main__":
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    unittest.main()