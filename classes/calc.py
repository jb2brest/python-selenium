

def somme(arg):
    resultat = 0
    for val in arg:
        resultat += val
    return resultat


def soustraction(arg1, arg2):
    resultat = arg1
    for val in arg2:
        resultat -= val
    return resultat


def multiplication(arg1, arg2):
    resultat = arg1 * arg2
    return resultat