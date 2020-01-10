korisnici = []
filmovi = []
projekcije = []
racuni = []
zanrovi = []


def ucitajEntitete():
    """
    funkcija sluzi za ucitavanje podataka iz tekstualnih fajlova
    """
    zanrovi.append({"ID": "1", "Zanr": "Akcioni"})
    zanrovi.append({"ID": "2", "Zanr": "Deciji"})
    zanrovi.append({"ID": "3", "Zanr": "Horor"})
    zanrovi.append({"ID": "4", "Zanr": "Romanticni"})

    try:
        f = open("../data/korisnici.txt", "r")
        podaci = f.readlines()
        for i in range(len(podaci)):
            # print(podaci[i])
            x = podaci[i].strip().split("|")
            # print (x)
            entitet = {"Korisnicko ime": x[0], "Sifra": x[1], "Ime": x[2], "Prezime": x[3], "Uloga": x[4]}
            # print(entitet)
            korisnici.append(entitet)
        f.close()
        f = open("../data/filmovi.txt", "r")
        podaci = f.readlines()
        for i in range(len(podaci)):
            x = podaci[i].strip().split("|")
            entitet = {"ID": x[0], "Naziv": x[1], "Zanr": x[2]}
            filmovi.append(entitet)
        f.close()

        f = open("../data/projekcije.txt", "r")
        podaci = f.readlines()
        for i in range(len(podaci)):
            x = podaci[i].strip().split("|")
            entitet = {"ID": x[0], "Datum pocetka": x[1], "Vreme pocetka": x[2], "Trajanje": int(x[3]),
                       "Cena": int(x[4]), "Film": x[5], "ID Sale": x[6], "Slobodna mesta": int(x[7]),
                       "Ukupno mesta": int(x[8]), "Obrisano logicki": x[9] == 'True'}
            projekcije.append(entitet)
        f.close()

        f = open("../data/racuni.txt", "r")
        podaci = f.readlines()
        for i in range(len(podaci)):
            x = podaci[i].strip().split("|")
            entitet = {"Sifra": x[0], "Datum": x[1], "Vreme prodaje": x[2], "Ukupna cena": x[3]}
            racuni.append(entitet)
        f.close()
    except IndexError:
        print("POGRESNI ULAZNI FAJLOVI")
        exit()


def snimiSveProjekcije():
    """
    funkcija sluzi za snimanje svih projekcija u fajl
    """
    f = open("../data/projekcije.txt", "w")
    for i in range(len(projekcije)):
        s = projekcije[i]["ID"] + "|" + projekcije[i]["Datum pocetka"] + "|" + projekcije[i][
            "Vreme pocetka"] + "|" + str(projekcije[i]["Trajanje"]) + "|" + str(projekcije[i]["Cena"]) + "|" + \
            projekcije[i]["Film"] + "|" + projekcije[i]["ID Sale"] + "|" + str(
            projekcije[i]["Slobodna mesta"]) + "|" + str(projekcije[i]["Ukupno mesta"]) + "|" + str(
            projekcije[i]["Obrisano logicki"]) + "\n"
        f.write(s)
    f.close()


def snimiFilmove():
    """
    funkcija sluzi za snimanje svih filmova u fajl
    """
    f = open("../data/filmovi.txt", "w")
    for i in range(len(filmovi)):
        s = filmovi[i]["ID"] + "|" + filmovi[i]["Naziv"] + "|" + filmovi[i]["Zanr"] + "\n"
        f.write(s)
    f.close()


def snimiRacune():
    """
    funkcija sluzi za snimanje svih racuna u fajl
    """
    f = open("../data/racuni.txt", "w")
    for i in range(len(racuni)):
        s = racuni[i]["Sifra"] + "|" + racuni[i]["Datum"] + "|" + racuni[i]["Vreme prodaje"] + "|" + str(
            racuni[i]["Ukupna cena"]) + "\n"
        f.write(s)
    f.close()