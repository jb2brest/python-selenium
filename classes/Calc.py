

class Calc:

    lastResult=0

    def __init__(self):
        lastResult=0

    def somme(self, arg):
        resultat = 0
        for val in arg:
            resultat += val
        self.lastResult = resultat
        return resultat

    def soustraction(self, arg1, arg2):
        resultat = arg1
        for val in arg2:
            resultat -= val
        self.lastResult = resultat
        return resultat

    def multiplication(self, arg1, arg2):
        resultat = arg1 * arg2
        self.lastResult = resultat
        return resultat