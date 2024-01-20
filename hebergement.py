from Date import Date


class hebergement:
    L = ['déjeuner', 'demi-pension', 'pension', 'complète']

    def __init__(self):
        self.Date_debut = Date(0, 0, 0)
        self.Nbre_de_nuit = ""
        self.Prix_nuit = ""
        self.active = True
        self.type = "hebergement"

    def saisir_Hébergement(self):

        self.Date_debut = self.Date_debut.Saisir_Date("Entrer la date du debut : ")
        self.Nbre_de_nuit = int(input("nombre de nuit est :"))

        for i, option in enumerate(self.L, 1):
            print(f"{i}. {option}")

        choix_type = int(input("Entrez le numéro du type choisit : "))

        self.type = self.L[choix_type - 1]
        self.Prix_nuit = float(input("prix par nuit:"))
        # self.prix_total = self.Prix_nuit * self.Nbre_de_nuit

    def afficher_hebergement(self):

        print("-----Les details d offre hebergement:-----")
        if self.active:

            print(' Date_debut:', self.Date_debut.strDate())
            print("Type:", self.type)
            print("Nombre de nuits: ", self.Nbre_de_nuit)
            # print("Prix total :", self.prix_total)

        else:
            print("L'offre est obsolète.")

    def str_hebergement(self):
        if self.active:
            dic_hebergement = {

                "Date de début: ": self.Date_debut.strDate(),
                "Type:": self.type,
                "Nombre de nuits: ": self.Nbre_de_nuit,
                'Type': self.type,
                'statut': self.active
                # "Prix total :": self.prix_total
            }
            return str(dic_hebergement)

        else:
            return "L'offre est obsolète."

    def saveINfileHEBER(self, nom_fichier="HEBERR.txt"):
        with open(nom_fichier, "a") as f:
            f.write(self.str_hebergement() + "\n")

    def saveINfileALLheber(self, nom_fichier="simpleeeee.txt"):
        with open(nom_fichier, "a") as f:
            f.write(self.str_hebergement() + "\n")

    def mettreAJourDateH(self):
        if self.active:
            nouvelle_dateDEBUT = Date(0, 0, 0)
            nouvelle_dateDEBUT.Saisir_Date("Entrez la nouvelle date")

            ancienne_date_str = self.Date_debut.strDate()  # Conserver l'ancienne date pour la recherche dans le fichier

            self.Date_debut = nouvelle_dateDEBUT

            # Lire le contenu du fichier
            with open("HEBERR.txt", "r") as fichier:
                lignes = fichier.readlines()

            # Mettre à jour les informations dans la liste des lignes
            for i, ligne in enumerate(lignes):
                if f"'Date ': '{ancienne_date_str}'" in ligne:
                    # Mettre à jour la ligne avec la nouvelle date
                    lignes[i] = self.str_hebergement() + "\n"
                    break  # Arrêter la boucle une fois la mise à jour effectuée

            # Réécrire le fichier avec les informations mises à jour
            with open("HEBERR.txt", "w") as fichier:
                fichier.writelines(lignes)

        else:
            print("L'offre est obsolète. Vous ne pouvez pas la mettre à jour.")

    def mettreAJourPrixH(self):
        if self.active:
            nouveau_Prix_nuit = float(input("Entrez le nouveau prix:"))
            ancien_prix = self.Prix_nuit  # Conserver l'ancien prix pour la recherche dans le fichier

            self.Prix_nuit = nouveau_Prix_nuit

            # Lire le contenu du fichier
            with open("HEBERR.txt", "r") as fichier:
                lignes = fichier.readlines()

            # Mettre à jour les informations dans la liste des lignes
            for i, ligne in enumerate(lignes):
                if f"'Prix': {ancien_prix}" in ligne:
                    # Mettre à jour la ligne avec le nouveau prix
                    lignes[i] = self.str_TransportAsimple() + "\n"
                    break  # Arrêter la boucle une fois la mise à jour effectuée

            # Réécrire le fichier avec les informations mises à jour
            with open("HEBERR.txt", "w") as fichier:
                fichier.writelines(lignes)
        else:
            print("L'offre est obsolète. Vous ne pouvez pas la mettre à jour.")

    def mettreAJourHEBER(self):
        if self.active:
            self.mettreAJourPrixH()
            self.mettreAJourDateH()
        else:
            print("L'offre est obsolète. Vous ne pouvez pas la mettre à jour.")

    def offre_obsoleteH(self):
        self.active = False
        print("L'offre a été bloquée.")

    def rendreObsolèteEtSauvegarderH(self):
        self.offre_obsoleteH()
        self.saveINfileHEBER()

    def afficher_offreS_save(self, nom_fichier='HEBERR.txt'):
        with open(nom_fichier, 'r') as f:
            print("----- Liste des offres sauvegardées d hebrgement  :-----")
            for i, line in enumerate(f, 1):
                print(f"{i}. {line.strip()}")
