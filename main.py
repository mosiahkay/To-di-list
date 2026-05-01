import json
import os

FICHIER_NOTES = "notes.json"

def charger_notes():
    if os.path.exists(FICHIER_NOTES):
        with open(FICHIER_NOTES, 'r', encoding='utf-8') as f:
            return json.load(f)
        return[]
    
def sauvegarder_notes(liste_notes):
    with open(FICHIER_NOTES, 'w', encoding=('utf-8')) as f:
        json.dump(liste_notes, f, indent=4, ensure_ascii=False)   

def  ajouter_note(liste_notes):
    note = input("veuillez ecrire une note:")
    liste_notes.append(note)
    sauvegarder_notes(liste_notes)
    print("Notes ajouter avec succes!")

def afficher_notes(liste_notes):
    print("Mes notes")
    print("-----------")
    if not liste_notes:
        print("Aucune note pour les moments")
        for i, note in enumerate(liste_notes, 1):
            print(f"{i}. {note}")
    
def supprimer_note(liste_notes):
    afficher_notes(liste_notes)
    if not liste_notes: return

    try:
        choix = int(input("Entrez le numero a supprimer:")) - 1
        if 0 <= choix < len(liste_notes):
            removed = liste_notes.pop(choix)
            sauvegarder_notes(liste_notes)
            print(f"Notes '{removed}' supprimee")
        else:
            print("numero invalide")
    except ValueError:
        print("Veuillez entrer un chiffre")

def modifier_note(liste_notes):
    afficher_notes()
    if not liste_notes: return
    try:
        choix = int(input("Veuillez choisir le numero a supprimer:")) - 1
        if 0 <= choix < len(liste_notes):
            nouveau_notes = input("Veuillez saisir le nouveau note:")
            liste_notes[choix] = nouveau_notes
            sauvegarder_notes(liste_notes)
            print("Note modifier!")
        else:
            print("Numero invalide")
    except ValueError:
        print("Veuillez entrer un chiffre")

def marquer_note():
    pass

def main():

    liste_notes = charger_notes()

    while True:
        print("\n 1. ajouter une note 2. afficher notes 3. supprimer notes 4. quitter")
        choix = input("Veuillez choisir une action:")
        if choix == "1":
            ajouter_note(liste_notes)
        elif choix == "2":
            afficher_notes(liste_notes)
        elif choix == "3":
            supprimer_note(liste_notes)
        elif choix == "4":
            print("Au revoir!")
            break
        else:
            print("choix invalide")

if __name__ == "__main__":
    main()