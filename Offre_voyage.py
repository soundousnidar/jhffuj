class Offre_voyage:

    def __init__(self):
        self.ref_offre = ""
        self.villeDepart = ""
        self.villeDarrivee = ""

    def saisirDonne(self):
        self.ref_offre = input("veuillez saisir la référence d offre:")
        self.villeDepart = input("veuillez saisir ville de depart:")
        self.villeDarrivee = input("veuillez saisir ville d arrivee:")

    def afficheOffre(self):
        print("_________ donne d offre voyage ________")
        print("ref_offre est: ", self.ref_offre)
        print("ville de depart est:", self.villeDepart)
        print("ville d arrivee est :", self.villeDarrivee)