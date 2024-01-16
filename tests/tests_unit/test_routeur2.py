import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from classes.Routeur import Routeur


def test_routage():
    # test de la fonction route 
    routeur = Routeur()
    routage=routeur.route("Habitation")
    attendu="Kevin"
    assert routage == attendu
    i = 1
    while i < 9:
        i = i + 1
        routage=routeur.route("Habitation")
        attendu="Kevin"
        assert routage == attendu
    routage=routeur.route("Habitation")
    attendu="Karenn"
    assert routage == attendu
    i = 1
    while i < 9:
        i = i + 1
        routage=routeur.route("Habitation")
        attendu="Karenn"
        assert routage == attendu
        
