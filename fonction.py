import re
from Etudiant import Etudiant

# Liste pour stocker les étudiants
etudiants = []

#insertion de donner sur le tableau d'etudiants pour la verifcation
etudiants.append(Etudiant("Aissatou", "Sow", "771234567", "Classe A", 15.0, 16.0, 14.5))
etudiants.append(Etudiant("Mamadou", "Diouf", "772345678", "Classe B", 12.5, 13.0, 11.0))
etudiants.append(Etudiant("Fatoumata", "Diallo", "773456789", "Classe A", 18.0, 19.0, 17.5))
etudiants.append(Etudiant("Ibrahima", "Ndiaye", "774567890", "Classe C", 10.0, 11.5, 12.0))
etudiants.append(Etudiant("Mariama", "Gueye", "775678901", "Classe B", 14.0, 15.0, 13.5))

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
    print("-"*137)
    print(f"{'Prénom':<15} {'Nom':<15} {'Téléphone':<15} {'Classe':<15} {'Devoir':<15} {'Projet':<15} {'Examen':<15} {'Moyenne':<15}")
    print("-"*137)
    for etudiant in etudiants:
        moyenne=(etudiant.devoir + etudiant.projet + etudiant.examen) / 3
        print(f"{etudiant.prenom:<15} {etudiant.nom:<15} {etudiant.telephone:<15} {etudiant.classe:<15} {etudiant.devoir:<15} {etudiant.projet:<15} {etudiant.examen:<15} {moyenne:<32}")
        print("-"*137)

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
            recherche_etudiant()
        elif choix == '4':
            modifier_notes()
        elif choix == '5':
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")        
  
  
            
#fonction pour trier et afficher les etudiants par ordre décroissant de la moyenne
def trier_etudiants_moyenne():
    etudiants.sort(key=lambda etudiant: etudiant.calculer_moyenne(), reverse=True)
    affiche_tab_etudiants()

#fonction pour rechercher un étudiant par téléphone, nom, prénom ou classe
def recherche_etudiant():
    verif=True
    while verif:
        critere = input("Critère de recherche (t : Téléphone, n : Nom, p : Prénom, c : Classe): ")
        
        if critere == 't':
            recherche_telephone()
            verif=False
        elif critere == 'n':
            recherche_nom()
            verif=False
        elif critere == 'p':
            recherche_prenom()
            verif=False
        elif critere == 'c':
            recherche_classe()
            verif=False
        else:
            print("Critère de recherche invalide.")
   
   
#fonction pour rechercher un étudiant par téléphone
def recherche_telephone():
    telephone = input("Téléphone à rechercher: ")
    while not est__numero_valide(telephone):
            print("Numéro de téléphone invalide. Veuillez verifier le numéro")
            telephone = input("Téléphone à rechercher: ")
    for etudiant in etudiants:
        if etudiant.telephone == telephone:
            etudiant.afficher_etudiant()
            return
    print("Etudiant non trouvé.")
    
#fonction pour rechercher un étudiant par nom
def recherche_nom():
    nom = input("Nom à rechercher: ")
    for etudiant in etudiants:
        if etudiant.nom.lower() == nom.lower():
            etudiant.afficher_etudiant()
            return
        print("Etudiant non trouvé.")

#fonction pour rechercher un étudiant par prénom
def recherche_prenom():
    prenom = input("Prénom à rechercher: ")
    for etudiant in etudiants:
        if etudiant.prenom.lower() == prenom.lower():
            etudiant.afficher_etudiant()
            return
        print("Etudiant non trouvé.")

#fonction pour rechercher un étudiant par classe
def recherche_classe():
    classe = input("Classe à rechercher: ")
    for etudiant in etudiants:
        if etudiant.classe.lower() == classe.lower():
            etudiant.afficher_etudiant()
            return
        print("Etudiant non trouvé.")
        
#fonction pour modifier les notes

def modifier_notes():
    telephone = input("Téléphone de l'étudiant: ")
    while not est__numero_valide(telephone):
            print("Numéro de téléphone invalide. Veuillez verifier le numéro")
            telephone = input("Téléphone de l'étudiant: ")
    if not est_etudiant_existe(telephone):
        print("Etudiant non trouvé.")
        return
    print("Quelle note souhaitez-vous modifier (d : Devoir, p : Projet, e : Examen)?")
    choix = input()
    if choix == 'd':
        modifier_element(telephone, 'devoir', float(input("Nouvelle note de devoir: ")))
    elif choix == 'p':
        modifier_element(telephone, 'projet', float(input("Nouvelle note de projet: ")))
    elif choix == 'e':
        modifier_element(telephone, 'examen', float(input("Nouvelle note d'examen: ")))


#fonction pour voir si un etudiant existe par son telephone
def est_etudiant_existe(telephone):
    for etudiant in etudiants:
        if etudiant.telephone == telephone:
            return True
    return False

#fonction pour modifier un element de l'etudiant
def modifier_element(telephone,element,valeur):
    for etudiant in etudiants:
        if etudiant.telephone == telephone:
            setattr(etudiant, element, valeur)
            print(element,"modifié avec succès.")
            return
            

    
    