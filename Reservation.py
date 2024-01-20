from Date import Date
class Reservation:
    K = ["en cours", "annulée", "confirmée"]

    def __init__(self):
        super().__init__()
        self.Ref_réservation = " "
        self.Type_Offre = "  "
        self.Ref_Offre = " "
        self.date_depart = Date(0, 0, 0)
        self.Date_retour = Date(0, 0, 0)
        self.Genre = ""
        self.Nom = ""
        self.Prénom = ""
        self.Pays_Nationalité = ""
        self.numPasseport = 0
        self.Etat_Reservation = ""
        self.Total_A_Payer = 0
        self.Prix_Transport = 0
        self.Prix_Hebergement = 0
        self.prix_total = 0
        self.type = "reservation "

    def saisir_reservation(self):
        Type_Offre = ["transport aller simple ", "transport aller retour", "hebrgement ", "formule complete"]
        self.Ref_réservation = input("Entrez la reference de reservation:")
        print("---choisir type d'offre : -----")
        for i, option in enumerate(Type_Offre, 1):
            print(f"{i}. {option}")
        choix_type_offre = int(input("Entrez le numero de votre choix  : "))
        self.Type_Offre = Type_Offre[choix_type_offre - 1]
        self.Ref_Offre = input("Entrez la référence d'offre : ")
        self.date_depart.Saisir_Date()

        if choix_type_offre == "2":
            print("Date de retour est :")
            self.Date_retour.Saisir_Date()

        self.Genre = input("Entrez votre genre:")
        self.Nom = input("Entrez votre nom:")
        self.Prénom = input("Entrez votre prenom:")
        self.Pays_Nationalité = input("Entrez votre Nationalité:")
        self.numPasseport = input("Entrez votre N passeport:")

        print("Choisissez le type :")
        for i, option in enumerate(self.K, 1):
            print(f"{i}. {option}")
        choix_type = int(input("Entrez le numéro d etat : "))

        self.Etat_Reservation = self.K[choix_type - 1]

        self.Prix_Transport = float(input("Entrez le prix du transport : "))
        self.Prix_Hebergement = float(input("Entrez le prix de l'hébergement : "))

        self.prix_total = self.Prix_Transport + self.Prix_Hebergement
        self.Total_A_Payer = 0.9 * self.prix_total

    def afficher_reservation(self):
        print("-----Les details de reservation.-----")

        print("la referance de la reservation est :", self.Ref_réservation)
        print("Votre type de reservation est :", self.Type_Offre)
        print("la referance d offre est :", self.Ref_Offre)
        print("la date de debut est :", self.date_depart.strDate())
        if self.Type_Offre == "transport aller retour":
            print("la date de retour est :", self.Date_retour.strDate())
        print("votre genre est:", self.Genre)
        print("le nom est :", self.Nom)
        print("le prenom est :", self.Prénom)
        print("le Pays de nationalit :", self.Pays_Nationalité)
        print("le numero de passepor est :", self.numPasseport)
        print("l etat de rervation est  :", self.Etat_Reservation)
        print("le total a payer est  :", self.Total_A_Payer)

    def enregistrer_reservation(self):
        reservation_dict = {
            "Ref_réservation": self.Ref_réservation,
            "Type_Offre": self.Type_Offre,
            "Ref_Offre": self.Ref_Offre,
            "Date_depart": self.date_depart.strDate(),
            "Date_retour": self.Date_retour.strDate() if self.Type_Offre == "transport aller retour" else None,
            "Genre": self.Genre,
            "Nom": self.Nom,
            "Prénom": self.Prénom,
            "Pays_Nationalité": self.Pays_Nationalité,
            "numPasseport": self.numPasseport,
            "Etat_Reservation": self.Etat_Reservation,
            "Total_A_Payer": self.Total_A_Payer,
            "Type": self.type
        }
        return str(reservation_dict)

    def save_reservation(self):
        with open("reservation.txt", "a") as f:
            f.write(self.enregistrer_reservation() + "\n")

    def afficher_reservation_save(self):
        with open('reservation.txt', 'r') as f:
            print("----- Liste des reservations :-----")
            for i, line in enumerate(f, 1):
                print(f"{i}. {line.strip()}")

    def lire_etat_reservation(self, ref_reservation):
        with open("reservation.txt", "r") as f:
            lignes = f.readlines()

        for ligne in lignes:
            reservation_dict = eval(ligne)  # Convert the string to a dictionary
            print(str(reservation_dict["Ref_réservation"]).strip())
            if str(reservation_dict["Ref_réservation"]).strip() == str(ref_reservation).strip():
                etat = reservation_dict.get("Etat_Reservation", None)

                return etat

    def confirmer_reservation(self, ref_reservation):
        etat_reservation = self.lire_etat_reservation(ref_reservation)
        if etat_reservation == "en cours":
            etat_reservation = "confirmée"
            print("La réservation a été confirmée.")
            return etat_reservation
        else:
            print("La réservation ne peut pas être confirmée car son état actuel n'est pas 'en cours'.")

    def annuler_reservation(self, ref_reservation):
        etat_reservation = self.lire_etat_reservation(ref_reservation)
        if etat_reservation == "en cours":
            etat_reservation = "annulée"
            print("La réservation a été annulée.")
            return etat_reservation
        else:
            print("La réservation ne peut pas être annulée car son état actuel n'est pas 'en cours'.")

    def update_reservation_state(self, ref_reservation, new_state):
        with open("reservation.txt", "r") as f:
            lignes = f.readlines()

        updated_content = []
        for ligne in lignes:
            reservation_dict = eval(ligne)  # Convert the string to a dictionary
            if str(reservation_dict["Ref_réservation"]).strip() == str(ref_reservation).strip():
                reservation_dict["Etat_Reservation"] = new_state
            updated_content.append(str(reservation_dict))

        with open("reservation.txt", "w") as f:
            f.writelines(updated_content)
