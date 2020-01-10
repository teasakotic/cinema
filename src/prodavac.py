import menadzer
import ucitavanje
import datetime


def ispisiMain():
    """
    funkcija sluzi za ispis opcija prodavca
    """
    print("1) Pretraga projekcija")
    print("2) Prodaja karata")
    print("3) Izlaz")


def prodajaKarata():
    """
    funkcija sluzi za funkcionalnost prodaje karte kod prodavca
    """
    ukupnaCena = 0
    prodato = {}
    while True:
        print()
        print("1) Prodaja karte: ")
        print("2) Izdaj racun: ")
        print("3) Povratak: ")
        odabir = input(">> ")
        if odabir == "1":
            menadzer.ispisiTabelu(menadzer.izbaciObrisane(ucitavanje.projekcije))
            while True:
                postoji = False
                slobodne = -1
                cena = -1
                sifra = input("Unesite sifru projekcije: ")
                if len(sifra) == 0:
                    print("Pogresan unos")
                    continue
                for i in ucitavanje.projekcije:
                    if i["ID"] == sifra and i["Obrisano logicki"] == False:
                        postoji = True
                        slobodne = i["Slobodna mesta"]
                        cena = i["Cena"]
                if postoji:
                    brojKarata = input("Unesite broj karata: ")
                    while menadzer.losaCena(brojKarata):
                        print("Los unos broja karata")
                        brojKarata = input("Unesite broj karata: ")
                    if int(brojKarata) <= slobodne:
                        ukupnaCena += int(brojKarata) * cena
                        for i in ucitavanje.projekcije:
                            if i["ID"] == sifra:
                                i["Slobodna mesta"] -= int(brojKarata)
                                ucitavanje.snimiSveProjekcije()
                        if not (sifra in prodato):
                            prodato[sifra] = int(brojKarata)
                        else:
                            prodato[sifra] += int(brojKarata)
                        break
                    else:
                        print("Nemamo toliko slobodnih sedista ")
        elif odabir == "2":
            if ukupnaCena != 0:
                datumVreme = datetime.datetime.today().strftime("%d.%m.%Y. %H:%M")
                datum = datumVreme.split(" ")[0]
                vreme = datumVreme.split(" ")[1]

                sifra = generisiSledecuSifru(ucitavanje.racuni)
                sifra = "R" + sifra
                for i in prodato:
                    sifra += " " + i + ";" + str(prodato[i])
                r = {"Sifra": sifra, "Datum": datum, "Vreme prodaje": vreme, "Ukupna cena": ukupnaCena}
                ucitavanje.racuni.append(r)
                ucitavanje.snimiRacune()
                print("Uspesno izdat racun")
            else:
                print("Kupite prvo nesto")
        elif odabir == "3":
            break
        else:
            print("Pogresan unos")


def generisiSledecuSifru(racuni):
    """
    funkcija sluzi za generisanje nove sifre kod pravljenja novog racuna
    """
    L = []
    for i in racuni:
        a = i["Sifra"].split(" ")[0]
        L.append(int(a[1:]))
    return str(max(L) + 1)


def opcije():
    """
    funkcija sluzi za osnovni meni kod prodavca
    """
    while True:
        ispisiMain()
        odabrano = input(">> ")
        if odabrano == "1":
            menadzer.pretragaProjekcija()
        elif odabrano == "2":
            prodajaKarata()
        elif odabrano == "3":
            break
        else:
            print("Los unos, pokusajte ponovo")
            print()
