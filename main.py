def  ajouter_note(liste_notes):
    note = input("veuillez ecrire une note:")
    liste_notes.append(note)
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
    choix = int(input("Veuillez entrer le numero de la note a supprimer :")) -1
    if 0 <= choix < len(liste_notes):
        del liste_notes[choix]
        print("Note supprimer")
    else:
        print("Numero invalide")

def modifier_note():
    pass
def marquer_note():
    pass

def main():

    liste_notes = []
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
    else:
        print("choix invalide")

if __name__ == "__main__":
    main()