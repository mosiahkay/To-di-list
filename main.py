import json
import os

FICHIER_NOTES = "notes.json"

def charger_notes():
    if os.path.exists(FICHIER_NOTES):
        try:
            with open(FICHIER_NOTES, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                else:
                    return data
        except json.JSONDecodeError:
            return[]
    return[]
    
def sauvegarder_notes(liste_notes):
    with open(FICHIER_NOTES, 'w', encoding='utf-8') as f:
        json.dump(liste_notes, f, indent=4, ensure_ascii=False)   

def  ajouter_note(liste_notes):
    texte = input("veuillez ecrire une note:")
    note = {"texte": texte, "terminee": False}
    liste_notes.append(note)
    sauvegarder_notes(liste_notes)
    print("Notes ajouter avec succes!")

def afficher_notes(liste_notes):
    print("Mes notes")
    print("-----------")
    if not liste_notes:
        print("Aucune note pour les moments")
    else:
        for i, note in enumerate(liste_notes, 1):
            statut = "✅" if note["terminee"] else "❌"
            print(f"{i}. {note['texte']} [{statut}]")
    
def supprimer_note(liste_notes):
    afficher_notes(liste_notes)
    if not liste_notes: 
        return

    try:
        choix = int(input("Entrez le numero a supprimer:")) - 1
        if 0 <= choix < len(liste_notes):
            removed = liste_notes.pop(choix)
            sauvegarder_notes(liste_notes)
            print(f"Note '{removed['texte']}' supprimée")
        else:
            print("numero invalide")
    except ValueError:
        print("Veuillez entrer un chiffre")

def modifier_note(liste_notes):
    afficher_notes(liste_notes)
    if not liste_notes: return
    try:
        choix = int(input("Veuillez choisir le numero a supprimer:")) - 1
        if 0 <= choix < len(liste_notes):
            nouveau_notes = input("Veuillez saisir le nouveau note:")
            liste_notes[choix]["texte"] = nouveau_notes
            sauvegarder_notes(liste_notes)
            print("Note modifier!")
        else:
            print("Numero invalide")
    except ValueError:
        print("Veuillez entrer un chiffre")

def marquer_note(liste_notes):
    afficher_notes(liste_notes)
    if not liste_notes:
        return

    try:
        choix = int(input("Numéro à marquer (Fait/À faire) : ")) - 1
        if 0 <= choix < len(liste_notes):
            # On inverse l'état actuel (Toggle)
            liste_notes[choix]["terminee"] = not liste_notes[choix]["terminee"]
            sauvegarder_notes(liste_notes)
            print("Statut mis à jour !")
        else:
            print("Numéro invalide")
    except ValueError:
        print("Veuillez entrer un chiffre")

def main():

    liste_notes = charger_notes()

    while True:
        print("\nMenu : 1.Ajouter | 2.Afficher | 3.Supprimer | 4.Modifier | 5.Terminer | 6.Quitter")
        choix = input("Veuillez choisir une action:")
        if choix == "1":
            ajouter_note(liste_notes)
        elif choix == "2":
            afficher_notes(liste_notes)
        elif choix == "3":
         supprimer_note(liste_notes)
        elif choix == "4":
            modifier_note(liste_notes)
        elif choix == "5":
            marquer_note(liste_notes)
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("choix invalide")

if __name__ == "__main__":
    main()