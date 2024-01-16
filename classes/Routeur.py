class Routeur:
    # Routeur permettant d'affecter des dossiers
    nbRoutage=0 # stocke le nombre de routage réalisé
    nbRoutageHabitation=0 # stocke le nombre de routage réalisé en habitation
    def __init__(self):
        nbRoutage=0
        nbRoutageHabitation=0

    
    # fonction de routage en fonction du type de dossier
    def route(self, type_dossier):
        self.nbRoutage = self.nbRoutage +1
        if type_dossier == "Habitation" :
            self.nbRoutageHabitation = self.nbRoutageHabitation + 1
            if self.nbRoutageHabitation < 10 :
                return "Kevin"
            else :
                return 'Karenn'
        else:
            return "Cyrille"