class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def Saisir_Date(self, msg="Entrez la date :"):
        print(msg)
        self.jour = int(input("jour: "))
        self.mois = int(input("mois: "))
        self.annee = int(input("annee: "))
        return Date(self.jour, self.mois, self.annee)

    def Saisir_Date_arrivee(self, msg="Entrez la date d'arrivee :"):
        print(msg)
        jour_arrivee = int(input("jour: "))
        mois_arrivee = int(input("mois: "))
        annee_arrivee = int(input("annee: "))
        return Date(jour_arrivee, mois_arrivee, annee_arrivee)

    def strDate(self):
        return f"{self.jour}/{self.mois}/{self.annee}"

    def strDateARIVEE(self):
        return f"{self.jour}/{self.mois}/{self.annee}"