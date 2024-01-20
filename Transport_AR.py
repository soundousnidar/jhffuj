
from Date import Date
from TransportAsimple import TransportAsimple


class Transport_AR(TransportAsimple):
    def __init__(self):
        super().__init__()
        self.date_arrivee = Date(0, 0, 0)
        self.active = True
        self.type = "aller_retour"

    def saisirDonne_AR(self):
        super().saisirDonne_simple()
        self.date_arrivee = self.date_arrivee.Saisir_Date_arrivee("Entrer la date d arrivee : ")

    def afficher_Transport_AR(self):

        if self.active:
            self.afficher_TransportAsimple()
            print('la date d arrivee :', self.date_arrivee.strDateARIVEE())
        else:
            print("L'offre est obsolète.")

    def str_Transport_AR(self):
        if self.active:
            dicTransport_AR = {
                "Ville de départ:": self.villeDepart,
                "Ville d'arrivée:": self.villeDarrivee,
                "Date de depart: ": self.date.strDate(),
                "Date d arrivee: ": self.date_arrivee.strDateARIVEE(),  # Keep it as a Date object
                "Prix:": self.prix,
                'Type': self.type,
                'Statut': self.active
            }
            return str(dicTransport_AR)
        else:
            return "L'offre est obsolète."

    def saveINfileAR(self, nom_fichier="ARRRR.txt"):
        with open(nom_fichier, "a") as f:
            f.write(self.str_Transport_AR() + "\n")

    def saveINfileALLar(self, nom_fichier="simpleeeee.txt"):
        with open(nom_fichier, "a") as f:
            f.write(self.str_Transport_AR() + "\n")

    def mettreAJourPrixAR(self):
        if self.active:
            nouveau_prix = float(input("Entrez le nouveau prix:"))
            ancien_prix = self.prix  # Conserver l'ancien prix pour la recherche dans le fichier

            self.prix = nouveau_prix

            # Lire le contenu du fichier
            with open("ARRRR.txt", "r") as fichier:
                lignes = fichier.readlines()

                # Mettre à jour les informations dans la liste des lignes
            for i, ligne in enumerate(lignes):
                if f"'Prix': {ancien_prix}" in ligne:
                    # Mettre à jour la ligne avec le nouveau prix
                    lignes[i] = self.str_Transport_AR() + "\n"
                    break  # Arrêter la boucle une fois la mise à jour effectuée

                    # Réécrire le fichier avec les informations mises à jour
                    with open("ARRRR.txt", "w") as fichier:
                        fichier.writelines(lignes)
            else:
                print("L'offre est obsolète. Vous ne pouvez pas la mettre à jour.")

    def mettreAJourDateAR(self):
        if self.active:
            # Update the departure date
            nouvelle_date_depart = Date(0, 0, 0)
            nouvelle_date_depart.Saisir_Date("Entrez la nouvelle date de départ")

            ancienne_date_depart_str = self.date.strDate()  # Conserver l'ancienne date pour la recherche dans le fichier

            self.date = nouvelle_date_depart

            # Lire le contenu du fichier
            with open("ARRRR.txt", "r") as fichier:
                lignes = fichier.readlines()

            # Mettre à jour les informations dans la liste des lignes
            for i, ligne in enumerate(lignes):
                if f"'Date de depart: ': '{ancienne_date_depart_str}'" in ligne:
                    # Mettre à jour la ligne avec la nouvelle date de départ
                    lignes[i] = self.str_Transport_AR() + "\n"
                    break  # Arrêter la boucle une fois la mise à jour effectuée

            # Réécrire le fichier avec les informations mises à jour
            with open("ARRRR.txt", "w") as fichier:
                fichier.writelines(lignes)

            # Update the arrival date
            nouvelle_date_arrivee = Date(0, 0, 0)
            nouvelle_date_arrivee.Saisir_Date("Entrez la nouvelle date d'arrivée")

            ancienne_date_arrivee_str = self.date_arrivee.strDateARIVEE()  # Conserver l'ancienne date pour la recherche dans le fichier

            self.date_arrivee = nouvelle_date_arrivee

            # Lire le contenu du fichier
            with open("ARRRR.txt", "r") as fichier:
                lignes = fichier.readlines()

            # Mettre à jour les informations dans la liste des lignes
            for i, ligne in enumerate(lignes):
                if f"'Date d arrivee: ': '{ancienne_date_arrivee_str}'" in ligne:
                    # Mettre à jour la ligne avec la nouvelle date d'arrivée
                    lignes[i] = self.str_Transport_AR() + "\n"
                    break  # Arrêter la boucle une fois la mise à jour effectuée

            # Réécrire le fichier avec les informations mises à jour
            with open("ARRRR.txt", "w") as fichier:
                fichier.writelines(lignes)

        else:
            print("L'offre est obsolète. Vous ne pouvez pas la mettre à jour.")

    def mettreAJourTransportAR(self):
        if self.active:
            self.mettreAJourPrixAR()
            self.mettreAJourDateAR()
        else:
            print("L'offre est obsolète. Vous ne pouvez pas la mettre à jour.")

    def offre_obsoleteAR(self):
        self.active = False
        print("L'offre a été bloquée.")

    def rendreObsolèteEtSauvegarderAR(self):
        self.offre_obsolete()
        self.saveINfileS()

    def afficher_offreS_saveAR(self):
        with open("ARRR.txt", 'r') as f:
            print("----- Liste des offres sauvegardées d offre aller routeur  :-----")
            for i, line in enumerate(f, 1):
                print(f"{i}. {line.strip()}")

