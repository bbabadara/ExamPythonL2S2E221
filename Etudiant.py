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
        print("-"*137)
        print(f"{'Prénom':<15} {'Nom':<15} {'Téléphone':<15} {'Classe':<15} {'Devoir':<15} {'Projet':<15} {'Examen':<15} {'Moyenne':<15}")
        print("-"*137)
        print(f"{self.prenom:<15} {self.nom:<15} {self.telephone:<15} {self.classe:<15} {self.devoir:<15} {self.projet:<15} {self.examen:<15} {self.calculer_moyenne():<32}")
        print("-"*137)
    #afficher plusieur etudiant
    def afficher_etudiants(self, etudiants):
        print("-"*137)
        print(f"{'Prénom':<15} {'Nom':<15} {'Téléphone':<15} {'Classe':<15} {'Devoir':<15} {'Projet':<15} {'Examen':<15} {'Moyenne':<15}")
        print("-"*137)
        for etudiant in etudiants:
            print(f"{etudiant.prenom:<15} {etudiant.nom:<15} {etudiant.telephone:<15} {etudiant.classe:<15} {etudiant.devoir:<15} {etudiant.projet:<15} {etudiant.examen:<15} {etudiant.calculer_moyenne():<32}")
            print("-"*137)
    


    