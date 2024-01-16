import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from classes.Calc import Calc

# Fichier de description des tests au format pytest pour la classe Calc

def test_somme():
    # test de la fonction somme 
    calc = Calc()
    calcul=calc.somme([1,2,3])
    attendu=6
    assert calcul == attendu


def test_somme_2():
    # test de la fonction somme
    calc = Calc()
    calcul=calc.somme([1,-2,3])
    attendu=6
    assert calcul != attendu

def test_soustraction():
    # test de la fonction soustraction
    calc = Calc()
    calcul=calc.soustraction(6,[1,2,3])
    attendu=0
    assert calcul == attendu