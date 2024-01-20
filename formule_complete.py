from Transport_AR import Transport_AR
from hebergement import hebergement


class Formule_complete(Transport_AR, hebergement):
    T = ["Week-End", "Semaine"]

    def __init__(self):
        super().__init__()

        self.type_formule = ""
        self.prix = 0
        self.type = "formule_complete"
        self.active = "True"

    def saisir_formuleComplete(self):
        super().saisirDonne_AR()

        for i, option in enumerate(self.T, 1):
            print(f"{i}. {option}")
        choix_type = int(input("Entrez le numéro du type choisi : "))
        self.type_formule = self.T[choix_type - 1]

    def afficher_formuleComplete(self):
        print("-----Les details d offre voyage complet.-----")
        if self.active:
            print("Ville de départ:", self.villeDepart)
            print("Ville d'arrivée:", self.villeDarrivee)
            print("Date de depart: ", self.date.strDate())
            print("Date d arrivee: ", self.date_arrivee.strDateARIVEE())
            print("Type:", self.type_formule)
            print("Prix:", self.prix)

        else:
            print("L'offre est obsolète.")

    def str_formuleComplete(self):
        if self.active:
            dic_complete = {
                "Ville de départ:": self.villeDepart,
                "Ville d'arrivée:": self.villeDarrivee,
                "Date de depart: ": self.date.strDate(),
                "Date d arrivee: ": self.date_arrivee.strDateARIVEE(),
                "Type formule:": self.type_formule,
                "Prix:": self.prix,
                'Type offre ': self.type,
                'statut': self.active

            }
            return str(dic_complete)
        else:
            return "L'offre est obsolète."

    def saveINfileFC(self, nom_fichier="FCCCC.txt"):
        with open(nom_fichier, "a") as f:
            f.write(self.str_formuleComplete() + "\n")

    def saveINfileALLfc(self, nom_fichier="simpleeeee.txt"):
        with open(nom_fichier, "a") as f:
            f.write(self.str_formuleComplete() + "\n")

    def mettreAJourPrixFC(self):
        if self.active:
            nouveau_prix = float(input("Entrez le nouveau prix:"))
            ancien_prix = self.prix  # Conserver l'ancien prix pour la recherche dans le fichier

            self.prix = nouveau_prix

            # Lire le contenu du fichier
            with open("FCCCC.txt", "r") as fichier:
                lignes = fichier.readlines()

            # Mettre à jour les informations dans la liste des lignes
            for i, ligne in enumerate(lignes):
                if f"'Prix': {ancien_prix}" in ligne:
                    # Mettre à jour la ligne avec le nouveau prix
                    lignes[i] = self.str_TransportAsimple() + "\n"
                    break  # Arrêter la boucle une fois la mise à jour effectuée

            # Réécrire le fichier avec les informations mises à jour
            with open("FCCCC.txt", "w") as fichier:
                fichier.writelines(lignes)
        else:
            print("L'offre est obsolète. Vous ne pouvez pas la mettre à jour.")

    def afficher_offreFC_save(self):
        with open('FCCCC.txt', 'r') as f:
            print("----- Liste des offres sauvegardées de formules completes :-----")
            for i, line in enumerate(f, 1):
                print(f"{i}. {line.strip()}")