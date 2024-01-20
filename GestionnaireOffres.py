from datetime import datetime


class GestionnaireOffres:
    def __init__(self):
        self.liste_offres = []
        self.liste_reservations = []

    # Méthode pour lire les offres depuis un fichier et les ajouter à la liste
    def charger_offres_depuis_fichier(self):
        with open("simpleeeee.txt", 'r') as f:
            for ligne in f:
                # Convertir la chaîne JSON en dictionnaire Python
                offre = eval(ligne.strip())
                self.ajouter_offre(offre)

    # Méthode pour ajouter une offre à la liste
    def ajouter_offre(self, offre):
        self.liste_offres.append(offre)

    def charger_reservations_depuis_fichier(self):
        with open("reservation.txt", 'r') as f:
            for ligne in f:
                # Convertir la chaîne JSON en dictionnaire Python
                reservation = eval(ligne.strip())

                self.ajouter_reservation(reservation)

    # Méthode pour ajouter une réservation à la liste
    def ajouter_reservation(self, reservation):
        self.liste_reservations.append(reservation)

    # Méthode pour compter les offres par type et le nombre total d'offres
    def calculer_statistiques_offres(self):
        nombre_offres_transport_ar = 0
        nombre_offres_simple = 0
        nombre_offres_hebergement = 0
        nombre_offres_formule_complete = 0
        nombre_offres_total = 0

        for offre in self.liste_offres:
            # Assurez-vous que chaque offre a une clé 'Type' dans son dictionnaire
            type_offre = offre.get('Type', '').lower()

            if 'aller_retour' in type_offre:
                nombre_offres_transport_ar += 1
            elif 'simple' in type_offre:
                nombre_offres_simple += 1
            elif 'hebergement' in type_offre:
                nombre_offres_hebergement += 1
            elif 'formule_complete' in type_offre :
                nombre_offres_formule_complete += 1



            nombre_offres_total += 1

        # Afficher les statistiques
        print("Nombre d'offres de Transport Aller-Retour:", nombre_offres_transport_ar)
        print("Nombre d'offres simples:", nombre_offres_simple)
        print("Nombre d'offres d'hebrgement:", nombre_offres_hebergement)
        print("Nombre d'offres de formule complete :", nombre_offres_formule_complete)
        print("Nombre total d'offres:", nombre_offres_total)

    def calculer_statistiques_reservations(self):
        nombre_reservations_annulees = 0
        nombre_reservations_confirmees = 0

        nombre_reservations_total = 0

        for reservation in self.liste_reservations:
            # Assurez-vous que chaque réservation a une clé 'Etat_Reservation' dans son dictionnaire
            etat_reservation = reservation.get('Etat_Reservation', '').lower()

            if 'annulée' in etat_reservation:
                nombre_reservations_annulees += 1
            elif 'confirmée' in etat_reservation:
                nombre_reservations_confirmees += 1

            nombre_reservations_total += 1

        # Afficher les statistiques
        print("Nombre de réservations annulées:", nombre_reservations_annulees)
        print("Nombre de réservations confirmées:", nombre_reservations_confirmees)

        print("Nombre total de réservations:", nombre_reservations_total)

    def calculer_chiffre_affaires_global(self):
        chiffre_affaires_global = 0

        for reservation in self.liste_reservations:
            total_a_payer = reservation.get('Total_A_Payer', 0)
            chiffre_affaires_global += total_a_payer
        print("Votre Chiffre d'affaires global : montant des gains est :", chiffre_affaires_global)
        return chiffre_affaires_global

    def calculer_chiffre_affaires_par_type(self):
        Type_Offre = ["transport aller simple ", "transport aller retour", "hebrgement ", "formule complete"]
        chiffre_affaires_par_type = {type_offre: 0 for type_offre in Type_Offre}

        for reservation in self.liste_reservations:
            total_a_payer = reservation.get('Total_A_Payer', 0)
            type_offre = reservation.get('Type_Offre', '').strip().lower()

            # Update the revenue for the corresponding type of offer
            if type_offre in Type_Offre:
                chiffre_affaires_par_type[type_offre] += total_a_payer

        # Print or return the results
        print("Chiffre d'affaires par type d'offre :")
        for type_offre, chiffre_affaires in chiffre_affaires_par_type.items():
            print(f"{type_offre}: {chiffre_affaires}")

        return chiffre_affaires_par_type

    def calculer_chiffre_affaires_par_nationalite(self):
        chiffre_affaires_par_nationalite = {}

        for reservation in self.liste_reservations:

            total_a_payer = reservation.get('Total_A_Payer', 0)
            nationalite = reservation.get('Pays_Nationalité', '').strip().lower()

            # Check if the nationality is not an empty string
            if nationalite:
                # Check if the nationality is already in the dictionary
                if nationalite in chiffre_affaires_par_nationalite:
                    chiffre_affaires_par_nationalite[nationalite] += total_a_payer
                else:
                    chiffre_affaires_par_nationalite[nationalite] = total_a_payer

        # Print or return the results
        print("Chiffre d'affaires par nationalité :")
        for nationalite, chiffre_affaires in chiffre_affaires_par_nationalite.items():
            print(f"{nationalite}: {chiffre_affaires}")

        return chiffre_affaires_par_nationalite

    def calculer_chiffre_affaires_par_periode(self):
        chiffre_affaires_par_periode = {}

        for reservation in self.liste_reservations:
            total_a_payer = reservation.get('Total_A_Payer', 0)
            date_depart = reservation.get('Date_depart', '').strip()

            # Convert date string to datetime object
            date_depart_obj = datetime.strptime(date_depart, '%d/%m/%Y') if date_depart else None

            # Check if the date is not empty
            if date_depart_obj:
                # Use the date as a key for the dictionary
                date_key = date_depart_obj.strftime('%d/%m/%Y')

                # Check if the date key is already in the dictionary
                if date_key in chiffre_affaires_par_periode:
                    chiffre_affaires_par_periode[date_key] += total_a_payer
                else:
                    chiffre_affaires_par_periode[date_key] = total_a_payer

        # Print or return the results
        print("Chiffre d'affaires par période :")
        for date_key, chiffre_affaires in chiffre_affaires_par_periode.items():
            print(f"{date_key}: {chiffre_affaires}")

        return chiffre_affaires_par_periode

    def filtrage_par_type(self):
        Type_Offre = ["simple", "aller retour", "hebergement", "formule complete"]
        for i, option in enumerate(Type_Offre, 1):
            print(f"{i}. {option}")

        choix_type_offre = int(input("Entrez le numéro de votre choix : "))
        type_choisi = Type_Offre[choix_type_offre - 1]

        # Initialiser le dictionnaire pour compter le nombre d'offres par type
        compteur_types = {type_: 0 for type_ in Type_Offre}

        for offre in self.liste_offres:
            type_offre_offre = offre.get('Type', '').lower()
            if type_offre_offre == type_choisi.lower():
                print("Offre disponible:", offre)
                # Incrémenter le compteur pour le type d'offre trouvé
                compteur_types[type_choisi] += 1

        # Afficher le nombre d'offres pour le type choisi
        print(f"Nombre d'offres de type '{type_choisi}': {compteur_types[type_choisi]}")

        # Afficher le nombre d'offres pour chaque type
        for type_, count in compteur_types.items():
            print(f"Nombre d'offres de type '{type_}': {count}")

    def filtrage_par_date_offre(self, date1, date2):
        offres_pour_periode = []
        for offre in self.liste_offres:
            print("offres dispo", offre)
            date_depart = offre.get('Date de depart', '').strip()
            date = offre.get('Date', '').strip()

            date_depart_obj = datetime.strptime(date_depart, '%d/%m/%Y') if date_depart else None
            date_obj = datetime.strptime(date, '%d/%m/%Y') if date else None

            # Check if the offer's dates are not empty before comparing
            if date_depart_obj and date_obj and (date1 <= date_depart_obj <= date2 or date1 <= date_obj <= date2):
                offres_pour_periode.append(offre)

        return offres_pour_periode

    def nbr_offre_par_periodes(self, date1, date2):
        offres_pour_periode = self.filtrage_par_date_offre(date1, date2)
        nombre_offres_pour_periode = len(offres_pour_periode)

        # Afficher le nombre d'offres pour la période spécifiée
        print(f"Nombre d'offres pour la période {date1} - {date2} : {nombre_offres_pour_periode}")

        return nombre_offres_pour_periode


    def filtrage_de_reservation_par_date(self, date1, date2):
        offres_pour_periode = []
        for offre in self.liste_reservations:
            date_depart = offre.get('Date depart', '').strip()

            date_depart_obj = datetime.strptime(date_depart, '%d/%m/%Y') if date_depart else None

            # Check if the offer's dates are not empty before comparing
            if date1 and date_depart_obj and date_depart_obj < datetime.strptime(date1, '%d/%m/%Y'):
                print(offre)
                offres_pour_periode.append(offre)
            else:
                print("Aucune réservation pour la période spécifiée")

        return offres_pour_periode

    def filtrage_reservations_par_client(self, nom, prenom):
        nbr_reservation_client = 0
        reservations_client = [reservation for reservation in self.liste_reservations
                               if reservation.get('Nom', '').lower() == nom.lower()
                               and reservation.get('Prénom', '').lower() == prenom.lower()]
        nbr_reservation_client += 1

        print("nombre de reservation pour le client cherche est ", nbr_reservation_client)

        return reservations_client

    def filtrage_reservations_par_nationalite(self, destination):
        nbr_reservation_natio = 0
        reservations_natio = [reservation for reservation in self.liste_reservations
                              if reservation.get('Pays_Nationalité', '').lower() == destination.lower()
                              ]
        nbr_reservation_natio += 1

        print("nombre de reservation pour la nationalite cherche cherche est ", nbr_reservation_natio)

        return reservations_natio


