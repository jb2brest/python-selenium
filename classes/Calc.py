

class Calc:
    # calculatrice permettant les sommes, soustractions et multiplications
    lastResult=0 # stocke le résultat du dernier calcul
    def __init__(self):
        lastResult=0

    # fonction additionnant la liste des nombres fournis en paramètre
    def somme(self, arg):
        resultat = 0
        for val in arg:
            resultat += val
        self.lastResult = resultat
        return resultat

    # Fonction soustrayant du premier argument la liste des nombres donnés en second argument
    def soustraction(self, arg1, arg2):
        resultat = arg1
        for val in arg2:
            resultat -= val
        self.lastResult = resultat
        return resultat

    # Fonction multipliant l'argument 1 par l'argument 2
    def multiplication(self, arg1, arg2):
        resultat = arg1 * arg2
        self.lastResult = resultat
        return resultat