import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import classes.calc as Calc

def test_somme():
    calc = Calc()
    calcul=calc.somme([1,2,3])
    attendu=6
    assert calcul == attendu

def test_soustraction():
    calc = Calc()
    calcul=calc.soustraction(6,[1,2,3])
    attendu=0
    assert calcul == attendu