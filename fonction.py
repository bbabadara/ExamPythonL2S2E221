import re
from Etudiant import Etudiant

# Liste pour stocker les étudiants
etudiants = []

#Fonction qui permet d'ajouter un etudiant
def ajout_etudiant():
    verif=True
    while verif:   
        prenom = input("Prénom: ")
        nom = input("Nom: ")
        telephone = input("Téléphone: ")
        while not est__numero_valide(telephone) or est_telephone_existant(telephone):
            print("Numéro de téléphone invalide. Veuillez verifier le numéro")
            telephone = input("Téléphone: ")
        
        classe = input("Classe: ")
        
        devoir = float(input("Note de devoir: "))
        while not est_note_valide(devoir):
            print("Les notes doivent être entre 0 et 20.")
            devoir = float(input("Note de devoir: "))
        
        projet = float(input("Note de projet: "))
        while not est_note_valide(projet):
            print("Les notes doivent être entre 0 et 20.")
            projet = float(input("Note de projet: "))
            
        examen = float(input("Note d'examen: "))
        while not est_note_valide(examen):
            print("Les notes doivent être entre 0 et 20.")
            examen = float(input("Note d'examen: "))
        
        etudiant = Etudiant(prenom, nom, telephone, classe, devoir, projet, examen)
        etudiants.append(etudiant)
        choix=input("Voulez-vous ajouter un autre etudiant? (o/n): ")
        if choix=="o":
            verif=True
        else:
           verif=False
           

#fonction qui verifie si le numero est valide
def est__numero_valide(numero):
    numero = numero.replace(" ", "")
    if len(numero) != 9:
        return False
    if not numero.startswith(('77', '78', '76', '70', '75')):
        return False
    return numero.isdigit()  

#fonction qui verifie si la note est comprie entre 0 et 20
def est_note_valide(note):
    return 0 <= note <= 20

#fonction qui verifie si le numero ne se trouve pas deja dans le tableau d'etudiant
def est_telephone_existant(numero):
    for etudiant in etudiants:
        if etudiant.telephone == numero:
            return True
    return False    
#Fontion qui affiche le tableau d'etudiant
def affiche_tab_etudiants():
    print("="*137)
    print(f"{'Prénom':<15} {'Nom':<15} {'Téléphone':<15} {'Classe':<15} {'Devoir':<15} {'Projet':<15} {'Examen':<15} {'Moyenne':<15}")
    print("="*137)
    for etudiant in etudiants:
        moyenne=(etudiant.devoir + etudiant.projet + etudiant.examen) / 3
        print(f"{etudiant.prenom:<15} {etudiant.nom:<15} {etudiant.telephone:<15} {etudiant.classe:<15} {etudiant.devoir:<15} {etudiant.projet:<15} {etudiant.examen:<15} {moyenne:<32}")
        print("="*137)

#fonction qui affiche le menu
def menu():
    while True:
        print("\nMenu:")
        print("1. Afficher tout")
        print("2. Afficher par ordre décroissant de la moyenne")
        print("3. Rechercher selon un critère")
        print("4. Modification de notes pour un étudiant")
        print("5. Sortir")
        
        choix = input("Choisissez une option: ")
        
        if choix == '1':
            affiche_tab_etudiants()
        elif choix == '2':
            trier_etudiants_moyenne()
        elif choix == '3':
            # rechercher_etudiant()
            print("3!")
        elif choix == '4':
            # modifier_notes()
            print("5!")
        elif choix == '5':
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")        
  
  
            
#fonction pour trier et afficher les etudiants par ordre décroissant de la moyenne
def trier_etudiants_moyenne():
    etudiants.sort(key=lambda etudiant: etudiant.calculer_moyenne(), reverse=True)
    affiche_tab_etudiants()
    