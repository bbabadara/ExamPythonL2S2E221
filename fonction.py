import re
from Etudiant import Etudiant

# Liste pour stocker les étudiants
etudiants = []

#Fonction qui permet d'ajouter un etudiant
def ajout_etudiant():
    prenom = input("Prénom: ")
    nom = input("Nom: ")
    telephone = input("Téléphone: ")
    while not est__numero_valide(telephone):
        print("Numéro de téléphone invalide. Veuillez entrer un numéro au format 772641040")
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

def est__numero_valide(numero):
    numero = numero.replace(" ", "")
    if len(numero) != 9:
        return False
    if not numero.startswith(('77', '78', '76', '70', '75')):
        return False
    return numero.isdigit()  

def est_note_valide(note):
    return 0 <= note <= 20


#Fontion qui affiche le tableau d'etudiant
def affiche_tab_etudiants():
    print("="*120)
    print(f"{'Prénom':<15} {'Nom':<15} {'Téléphone':<15} {'Classe':<15} {'Devoir':<15} {'Projet':<15} {'Examen':<15} {'Moyenne':<15}")
    print("="*120)
    for etudiant in etudiants:
        moyenne=(etudiant.devoir + etudiant.projet + etudiant.examen) / 3
        print(f"{etudiant.prenom:<15} {etudiant.nom:<15} {etudiant.telephone:<15} {etudiant.classe:<15} {etudiant.devoir:<15} {etudiant.projet:<15} {etudiant.examen:<15} {moyenne:<15}")
        print("="*120)
        