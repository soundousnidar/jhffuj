from GestionnaireOffres import GestionnaireOffres
from Reservation import Reservation
from TransportAsimple import TransportAsimple
from Transport_AR import Transport_AR
from formule_complete import Formule_complete
from hebergement import hebergement

while True:
    print("-----Menu principal:--------")
    print("1- Déclarer une offre de voyage")
    print("2- Mettre à jour une offre de voyage")
    print("3- Bloquer une offre de voyage")
    print("4- Afficher une offre selon son type")
    print("5- Afficher les offres avec filtres")
    print("6- Faire une réservation")
    print("7- Confirmer ou annuler une réservation")
    print("8- Calculer les statistiques")
    print("9- Quitter")

    choix = input("Choisissez une option (1-9) : ")

    if choix == "1":

        print("------menu des offres------")
        print("1-Transport Aller Simple ")
        print("2-Transport Aller / Retour")
        print("3-Hébergement")
        print("4-Formule complète")
        choix1 = input("Choisissez une option (1-4) : ")

        if choix1 == "1":
            offre_simple = TransportAsimple()
            offre_simple.saisirDonne_simple()
            offre_simple.afficher_TransportAsimple()
            offre_simple.saveINfileS()
            offre_simple.saveINfileALLS()

        elif choix1 == "2":
            offre_AR = Transport_AR()
            offre_AR.saisirDonne_AR()
            offre_AR.afficher_Transport_AR()
            offre_AR.saveINfileAR()
            offre_AR.saveINfileALLar()

        elif choix1 == "3":
            offre_HEBER = hebergement()
            offre_HEBER.saisir_Hébergement()
            offre_HEBER.afficher_hebergement()
            offre_HEBER.saveINfileHEBER()
            offre_HEBER.saveINfileALLheber()

        elif choix1 == "4":
            offre_complet = Formule_complete()
            offre_complet.saisir_formuleComplete()
            offre_complet.afficher_formuleComplete()
            offre_complet.saveINfileFC()
            offre_complet.saveINfileALLfc()

        else:
            print("Choix invalide.")

    elif choix == "2":
        print("Choisissez le type d offre a mettre a jour :")
        print("1- Transport simple")
        print("2- Transport A/R")
        print("3- Hébergement")
        print("4- Formule complète")

        choix2 = input("Entrez le numéro du type d'offre à mettre à jour : ")

        if choix2 == "1":
            print("voulez vous mette a jour:")
            print("1- le prix:")
            print("2- la date:")
            print("3- la date et le prix:")
            choix21 = input("Entrez le numero a mettre à jour : ")

            if choix21 == "1":
                transport_simple = TransportAsimple()
                transport_simple.mettreAJourPrix()
                transport_simple.saveINfileS()
                transport_simple.saveINfileALLS()

            elif choix21 == "2":
                transport_simple = TransportAsimple()
                transport_simple.mettreAJourDate()
                transport_simple.saveINfileS()
                transport_simple.saveINfileALLS()

            elif choix21 == "3":
                transport_simple = TransportAsimple()
                transport_simple.mettreAJourTransportAsimple()
                transport_simple.saveINfileS()
                transport_simple.saveINfileALLS()

            else:
                print("Choix invalide.")

        elif choix2 == "2":
            print("voulez vous mette a jour:")
            print("1- le prix:")
            print("2- la date:")
            print("3- la date et le prix:")
            choix22 = input("Entrez le numero a mettre à jour : ")

            if choix22 == "1":
                transport_AR = Transport_AR()
                transport_AR.mettreAJourPrix()
                transport_AR.saveINfileAR()
                transport_AR.saveINfileALLar()

            elif choix22 == "2":
                transport_AR = Transport_AR()
                transport_AR.mettreAJourDateAR()
                transport_AR.mettreAJourDate()
                transport_AR.saveINfileAR()
                transport_AR.saveINfileALLar()

            elif choix22 == "3":
                transport_AR = Transport_AR()
                transport_AR.mettreAJourDateAR()
                transport_AR.mettreAJourPrixAR()
                transport_AR.saveINfileAR()
                transport_AR.saveINfileALLar()

            else:
                print("Choix invalide.")

        elif choix2 == "3":
            print("voulez vous mette a jour:")
            print("1- le prix:")
            print("2- la date:")
            print("3- la date et le prix:")
            choix23 = input("Entrez le numero a mettre à jour : ")

            if choix23 == "1":
                HEBER = hebergement()
                HEBER.mettreAJourPrixH()
                HEBER.saveINfileHEBER()
                HEBER.saveINfileALLheber()

            elif choix23 == "2":
                HEBER = hebergement()
                HEBER.mettreAJourDateH()
                HEBER.saveINfileHEBER()
                HEBER.saveINfileALLheber()

            elif choix23 == "3":
                HEBER = hebergement()
                HEBER.mettreAJourHEBER()
                HEBER.saveINfileHEBER()
                HEBER.saveINfileALLheber()

            else:
                print("Choix invalide.")

        elif choix2 == "4":
            print("voulez vous mette a jour:")
            print("1- le prix:")
            print("2- la date:")
            print("3- la date et le prix:")
            choix24 = input("Entrez le numero a mettre à jour : ")

            if choix24 == "1":
                complete = Formule_complete()
                complete.mettreAJourPrixFC()
                complete.saveINfileFC()
                complete.saveINfileALLfc()

            elif choix24 == "2":
                complete = Formule_complete()
                complete.mettreAJourDateH()
                complete.saveINfileFC()
                complete.saveINfileALLfc()

            elif choix24 == "3":
                complete = Formule_complete()
                complete.mettreAJourDateH()
                complete.mettreAJourPrixFC()
                complete.saveINfileFC()
                complete.saveINfileALLfc()

            else:
                print("Choix invalide.")



    elif choix == "3":
        print("Choisissez le type d offre a Bloquer :")
        print("1- Transport simple")
        print("2- Transport A/R")
        print("3- Hébergement")
        print("4- Formule complète")

        choix3 = input("Entrez le numéro du type d'offre a bloquer : ")

        if choix3 == "1":
            bloquerS = TransportAsimple()
            bloquerS.afficher_TransportAsimple()
            bloquerS.rendreObsolèteEtSauvegarder()
            bloquerS.afficher_TransportAsimple()

        elif choix3 == "2":
            bloquerAR = Transport_AR()
            bloquerAR.afficher_Transport_AR()
            bloquerAR.rendreObsolèteEtSauvegarderAR()
            bloquerAR.afficher_Transport_AR()

        elif choix3 == "3":
            bloquerHEBER = hebergement()
            bloquerHEBER.afficher_hebergement()
            bloquerHEBER.rendreObsolèteEtSauvegarderH()
            bloquerHEBER.afficher_hebergement()

        elif choix3 == "4":
            bloquerFC = Formule_complete()
            bloquerFC.afficher_formuleComplete()

            bloquerFC.afficher_formuleComplete()
        else:
            print("Choix invalide.")



    elif choix == "4":
        print("Choisissez le type d offre a afficher :")
        print("1- Transport simple")
        print("2- Transport A/R")
        print("3- Hébergement")
        print("4- Formule complète")

        choix4 = input("Entrez le numéro du type d'offre a afficher : ")

        if choix4 == "1":
            afficherS = TransportAsimple()
            afficherS.afficher_offreS_save()

        elif choix4 == "2":
            afficherAR = Transport_AR()
            afficherAR.afficher_offreS_saveAR()

        elif choix4 == "3":
            afficherHEBER = hebergement()
            afficherHEBER.afficher_offreS_save()

        elif choix == "4":
            afficherFC = Formule_complete()
            afficherFC.afficher_offreFC_save()


    elif choix == "6":

        reserve = Reservation()
        reserve.saisir_reservation()
        reserve.afficher_reservation()
        reserve.save_reservation()

    elif choix == "7":
        print("---- confirmer ou annuler une reservation :-----")
        print("1- confirmer reservation")
        print("2- annuler  reservation")
        choix7 = input("chosir votre action : ")
        reservation = Reservation()
        if choix7 == "1":
            reservation.afficher_reservation_save()
            ref = input("choisir la reference de reservation a modifier son etat :")
            new_state = reservation.confirmer_reservation(ref)
            reservation.update_reservation_state(ref, new_state)

        else:
            reservation.afficher_reservation_save()
            ref = input("choisir la reference de reservation a modifier son etat :")
            new_state = reservation.annuler_reservation(ref)
            reservation.update_reservation_state(ref, new_state)

    elif choix == "8" :
        print("------ Calcule des statistiques suivantes : ------")
        print("1- Nbre d'offres par type et Nbre d'offres total.")
        print("2- Nbre d'offres pour une période précise.")
        print("3- Nbre de réservations annulées, confirmées ou Global.")
        print("4- Nbre de réservations confirmées par période,  par client  ou par nationalité.")
        print("5- Chiffre d'affaires global : montant des gains.")
        print("6- Chiffre d'affaires global par période, par type, par destination et/ou par nationalité.")
        print("7-Quitter")
        choix8 = input("chosir votre statistiques a afficher  : ")
        if choix8 == "1":
            nbr_offre = GestionnaireOffres()
            nbr_offre.charger_offres_depuis_fichier()
            nbr_offre.calculer_statistiques_offres()
        elif choix8 == '2':
            nbr_offre_periode = GestionnaireOffres()
            nbr_offre_periode.charger_offres_depuis_fichier()
            date1 = input("Entrez la date de début (format DD/MM/YYYY) : ")
            date2 = input("Entrez la date de fin (format DD/MM/YYYY) : ")
            nbr_offre_periode.nbr_offre_par_periodes(date1, date2)
        elif choix8 == '3' :
            nbr_reservation = GestionnaireOffres()
            nbr_reservation.charger_reservations_depuis_fichier()
            nbr_reservation.calculer_statistiques_reservations()
        elif choix8 == "4":
            nbr_reservation_filtree = GestionnaireOffres()
            nbr_reservation_filtree.charger_reservations_depuis_fichier()
            print("------voir nbr reservations : -------")
            print("1-par nationalite :")
            print("2-par client :")
            print("3- par date :")
            choix = input("choisir type de filtrage :")
            if choix == "1" :
                nationalite = input("saisir la nationalite:")
                nbr_reservation_filtree.filtrage_reservations_par_nationalite(nationalite)
            elif choix == "2":
                nom = input("entrez nom client:")
                prenom = input("entrez prenom client:")
                nbr_reservation_filtree.filtrage_reservations_par_client(nom,prenom)
            else:
                date1 = input("Entrez la date de début (format DD/MM/YYYY) : ")
                date2 = input("Entrez la date de fin (format DD/MM/YYYY) : ")
                nbr_reservation_filtree.filtrage_de_reservation_par_date(date1,date2)
        elif choix8 == "5":
            chiffre_daffiaires = GestionnaireOffres()
            chiffre_daffiaires.charger_reservations_depuis_fichier()
            chiffre_daffiaires.calculer_chiffre_affaires_global()
        elif choix8 == "6":
            chiffre_daffiaires_filtree = GestionnaireOffres()
            chiffre_daffiaires_filtree.charger_reservations_depuis_fichier()
            chiffre_daffiaires_filtree.calculer_chiffre_affaires_par_nationalite()
            chiffre_daffiaires_filtree.calculer_chiffre_affaires_par_periode()
            chiffre_daffiaires_filtree.calculer_chiffre_affaires_par_type()


