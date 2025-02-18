print("[i] Bienvenue sur le jeux PyConsole, ce jeux est un jeux a choix simple qui se deroulera dans votre console (cmd).")
print("[i] Ce jeux a été codé en python")
Patch = "1"

def Menu():
    Play = input("[J/Q/V] Jouer / Quitter / Version: ")

def PlayerName():
    name = input("[i] Veuillez choisir le nom de votre joueur: ")
    print("[?] Votre prenom est bien",name)
    nameval = input("[O/N] Oui / Non: ")
    if nameval == "O":
        print("Parfait !, le jeux peux commencer")
    elif nameval == "N":
        PlayerName()
    
if Menu(Play="Y") == "J":
    PlayerName()

elif Menu(Play="Q") == "Q":
    print("[i] Vous venez de quitter le jeux avec succés")

elif Menu():
    print("Version actuel ",Patch)
    Back = input("[O/N] Retourner en arriere ?: ")
    if Back == "O":
        Play
     
def GameBegin():
    print("")
