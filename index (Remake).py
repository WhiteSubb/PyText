print("[i] Bienvenue sur le jeux PyConsole, ce jeux est un jeux a choix simple qui se deroulera dans votre console (cmd).")
print("[i] Ce jeux a été codé en python")

Play = input("[J/Q] Jouer / Quitter: ")
name = ""

def PlayerName():
    name = input("[i] Veuillez choisir le nom de votre joueur: ")
    print("[?] Votre prenom est bien",name)
    nameval = input("[O/N] Oui / Non: ")
    if nameval == "O":
        print("Parfait !, le jeux peux commencer")
        GameStarted()
    elif nameval == "N":
        PlayerName()
    
def GameStarted():
    print(name)
    
if Play == "J":
    PlayerName()

elif Play == "Q":
    print("[i] Vous venez de quitter le jeux avec succés")
