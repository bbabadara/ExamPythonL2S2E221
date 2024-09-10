class Etudiant:
    def __init__(self, prenom, nom, telephone, classe, devoir, projet, examen):
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone
        self.classe = classe
        self.devoir = devoir
        self.projet = projet
        self.examen = examen
       
    
    def calculer_moyenne(self):
        return (self.devoir + self.projet + self.examen) / 3
    
    def afficher_etudiant(self):
        print(f"Prénom: {self.prenom}, Nom: {self.nom}, Téléphone: {self.telephone}, Classe: {self.classe}, "
              f"Devoir: {self.devoir}, Projet: {self.projet}, Examen: {self.examen}, Moyenne: {self.calculer_moyenne():.2f}")
    
# etudiant=Etudiant("Badara","Ba",772641040,"L2Dev",15.5,16,17)
# etudiant.afficher_etudiant()
# print(etudiant)

    