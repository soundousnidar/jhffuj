
from Date import Date
from Offre_voyage import Offre_voyage


class TransportAsimple(Offre_voyage):
    def __init__(self):
        super().__init__()
        self.date = Date(0, 0, 0)
        self.prix = 0
        self.active = True
        self.type = "simple"

    def saisirDonne_simple(self):

        self.saisirDonne()
        self.date.Saisir_Date()
        self.prix = float(input("Entrez le prix:"))

    def afficher_TransportAsimple(self):

        if self.active:

            self.afficheOffre()
            print("Date debut/ depart :", self.date.strDate())
            print("Prix:", self.prix)
        else:
            print("L'offre est obsolète.")

    def str_TransportAsimple(self):
        if self.active:
            dicTransportAsimple = {
                'Ville de départ': self.villeDepart,
                'Ville d arrivée': self.villeDarrivee,
                'Date ': self.date.strDate(),
                'Prix': self.prix,
                'Type': self.type,
                'statut': self.active

            }
            return str(dicTransportAsimple)
        else:
            return "L'offre est obsolète."

    def saveINfileS(self, nom_fichier="simple.txt"):
        with open(nom_fichier, "a") as f:
            f.write(self.str_TransportAsimple() + "\n")

    def saveINfileALLS(self, nom_fichier="simpleeeee.txt"):
        with open(nom_fichier, "a") as f:
            f.write(self.str_TransportAsimple() + "\n")

    def mettreAJourPrix(self):
        if self.active:
            # Lire le contenu du fichier
            with open("simple.txt", "r") as fichier:
                lignes = [ligne.strip() for ligne in fichier.readlines()]
                prices = []

                # Trouver l'index de la ligne contenant le prix
                index_prix = -1
                for i, ligne in enumerate(lignes):
                    if "'Prix':" in ligne:
                        index_prix = i
                        # Extract only the numeric part of the string representing the price
                        prix_str = ligne.split("'Prix':")[1].split(",")[0].strip()
                        ancien_prix = float(prix_str)
                        prices.append(ancien_prix)

            print("prices ", prices)
            # Demander à l'utilisateur d'entrer le nouveau prix
            nouveau_prix = float(input("Entrez le nouveau prix:"))

            # Mettre à jour la liste 'prices' avec le nouveau prix
            for i in range(len(prices)):
                prices[i] = nouveau_prix
                print("neww", prices)

            # Mettre à jour l'attribut de l'objet avec le nouveau prix
            self.prix = nouveau_prix

            # Mettre à jour la ligne dans le fichier avec le nouveau prix
            if index_prix != -1:
                lignes[index_prix] = lignes[index_prix].replace(str(ancien_prix), str(nouveau_prix))

                # Réécrire le fichier avec les nouvelles valeurs de prix
                with open("simple.txt", "w") as fichier:
                    for ligne in lignes:
                        fichier.write(ligne + "\n")

        else:
            print("L'offre est obsolète. Vous ne pouvez pas la mettre à jour.")

    def mettreAJourDate(self):
        if self.active:
            nouvelle_date = Date(0, 0, 0)
            nouvelle_date.Saisir_Date("Entrez la nouvelle date")

            ancienne_date_str = self.date.strDate()  # Conserver l'ancienne date pour la recherche dans le fichier

            self.date = nouvelle_date

            # Lire le contenu du fichier
            with open("simpleeeee.txt", "r") as fichier:
                lignes = fichier.readlines()

            # Mettre à jour les informations dans la liste des lignes
            for i, ligne in enumerate(lignes):
                if f"'Date ': '{ancienne_date_str}'" in ligne:
                    # Mettre à jour la ligne avec la nouvelle date
                    lignes[i] = self.str_TransportAsimple() + "\n"
                    break  # Arrêter la boucle une fois la mise à jour effectuée

            # Réécrire le fichier avec les informations mises à jour
            with open("simpleeeee.txt", "w") as fichier:
                fichier.writelines(lignes)

        else:
            print("L'offre est obsolète. Vous ne pouvez pas la mettre à jour.")

    def mettreAJourTransportAsimple(self):
        if self.active:
            self.mettreAJourPrix()
            self.mettreAJourDate()
        else:
            print("L'offre est obsolète. Vous ne pouvez pas la mettre à jour.")

    def offre_obsolete(self):
        self.active = False
        print("L'offre a été bloquée.")

    def rendreObsolèteEtSauvegarder(self):
        self.offre_obsolete()
        self.saveINfileS()

    def afficher_offreS_save(self, nom_fichier='simple.txt'):
        with open(nom_fichier, 'r') as f:
            print("----- Liste des offres sauvegardées d offre simple  :-----")
            for i, line in enumerate(f, 1):
                print(f"{i}. {line.strip()}")