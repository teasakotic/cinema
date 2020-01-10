import ucitavanje
import datetime
import copy

def dajDuzinuHedera(entiteti):
    """
    funkcija sluzi za pronalazak maksimalnih duzina kod kolona prilikom ispisivanja tabele
    """
    if len(entiteti) == 0:
        return "Nema pronadjenih rezultata"
    M = []
    for i in range(len(entiteti[0])):
        M.append([])
    j = 0
    for i in (entiteti[0]):
        M[j].append(len(i))
        j += 1
    for i in range(len(entiteti)):
        br = 0
        for j in entiteti[i]:
            M[br].append(len(str(entiteti[i][j])))
            br += 1
    R = []
    for i in M:
        R.append(max(i))
    return R


def ispisiMain():
    """
    funkcija sluzi za prikaz funkcionalnosti kod menadzera
    """
    print()
    print("1) Pretraga projekcija: ")
    print("2) Unos nove projekcije: ")
    print("3) Brisanje projekcije: ")
    print("4) Izmena projekcije: ")
    print("5) Izlaz: ")
    print()


def izbaciObrisane(svi):
    """
    funkcija sluzi za izbacivanje obrisanih projekcija
    """
    rez = []
    temp = copy.deepcopy(svi)
    for i in temp:
        if not i["Obrisano logicki"]:
            del i["Obrisano logicki"]
            rez.append(i)
    return rez


def ispisiTabelu(listaEntiteta):
    """
    funkcija sluzi za tabelarnih prikaz liste entiteta
    """
    test = listaEntiteta
    heder = list(test[0].keys())
    if len(heder) > 5:
        zameniSveIdsaFilmom(test)

    lista = dajDuzinuHedera(test)
    if type(lista) == str:
        print(lista)
        return
    lista = dajDuzinuHedera(test)
    duzinaCrtica = (sum(lista) + len(heder) + 1)

    s = "|"
    print("-" * duzinaCrtica)
    for i in range(len(heder)):
        s += "{heder[" + str(i) + "]:^{lista[" + str(i) + "]}}|"
    print(s.format(heder=heder, lista=lista))
    for i in range(len(test)):
        print("-" * duzinaCrtica)
        s = "|"
        for j in range(len(heder)):
            s += "{AD[" + str(j) + "]:^{lista[" + str(j) + "]}}|"
        print(s.format(lista=lista, AD=list(test[i].values())))
    print("-" * duzinaCrtica)


def pronadjiPoId(lista):
    """
    funkcija sluzi za pronalazak projekcije po sifri
    """
    pronasao = True
    sifra = input("Unesite sifru projekcije: ")
    while len(sifra.strip()) == 0:
        print("Los unos")
        sifra = input("Unesite sifru projekcije: ")
    for i in range(len(lista)):
        if lista[i]["ID"] == sifra:
            pronasao = False
            L = [lista[i]]
            ispisiTabelu(izbaciObrisane(L))
    if pronasao:
        print("Ne postoji projekcija sa tim ID-om ")


def dajNazivFilma(id):
    """
    funkcija sluzi za pronalazak naziva filma po idu filma
    """
    filmovi = ucitavanje.filmovi
    for i in range(len(filmovi)):
        if filmovi[i]["ID"] == id:
            return filmovi[i]["Naziv"]


def pronadjiPoFilmu(lista):
    """
    funkcija sluzi za pronalazak svih filmova po unetom kriterijumu za film
    """
    pronasao = True
    L = []
    naziv = input("Unesite naziv filma: ")
    while len(naziv.strip()) == 0:
        print("Loz unos")
        naziv = input("Unesite naziv filma: ")
    for i in range(len(lista)):
        if naziv.lower() in dajNazivFilma(lista[i]["Film"]).lower():
            pronasao = False
            L.append(lista[i])
    if pronasao:
        print("Ne postoji projekcija sa tim nazivom filma ")
    else:
        ispisiTabelu(izbaciObrisane(L))


def vratiFilmoveZanr(param):
    """
    funkcija sluzi za pronalzak svih filmova po datom zanru
    """
    filmovi = ucitavanje.filmovi
    r = []
    for i in range(len(filmovi)):
        if filmovi[i]["Zanr"] == param:
            r.append(filmovi[i]["ID"])
    return r


def pronadjiPoZanru(lista):
    """
    funkcija sluzi za pronalazak svih projekcija po izabranom zanru
    """
    print()
    print("Moguci zanrovi: ")

    ispisiTabelu(ucitavanje.zanrovi)
    filmovi = []
    opcija = input(">> ")
    if opcija == "1":
        filmovi = vratiFilmoveZanr("Akcioni")
    elif opcija == "2":
        filmovi = vratiFilmoveZanr("Deciji")
    elif opcija == "3":
        filmovi = vratiFilmoveZanr("Horor")
    elif opcija == "4":
        filmovi = vratiFilmoveZanr("Romanticni")
    else:
        print("Pogresan unos")

    pronasao = True
    L = []
    for j in filmovi:
        for i in range(len(lista)):
            if lista[i]["Film"] == j:
                pronasao = False
                L.append(lista[i])
    if pronasao:
        print("Ne postoji projekcija sa tim zanrom filma ")
    else:
        ispisiTabelu(izbaciObrisane(L))


def pronadjiPoSali(lista):
    """
    funkcija sluzi za pronalazak svih projekcija po unetoj sali
    """
    pronasao = True
    L = []
    naziv = input("Unesite naziv sale: ")
    for i in range(len(lista)):
        if naziv.lower() in lista[i]["ID Sale"].lower():
            pronasao = False
            L.append(lista[i])
    if pronasao:
        print("Ne postoji projekcija sa tim nazivom sale ")
    else:
        ispisiTabelu(izbaciObrisane(L))


def zameniSveIdsaFilmom(projekcije):
    """
    funkcija sluzi za promenu svih id-ova filma, sa nazivom filma
    """
    for i in projekcije:
        i["Film"] = dajNazivFilma(i["Film"])


def pretragaProjekcija():
    """
    funkcija sluzi za osnovni prikaz i odabri kod pretraga projekcija
    """
    lista = ucitavanje.projekcije
    print("1) ID-ju projekcije")
    print("2) Nazivu filma")
    print("3) Zanru filma ")
    print("4) Sali prikazivanja")
    odabrano = input(">> ")
    if odabrano == "1":
        pronadjiPoId(lista)
    elif odabrano == "2":
        pronadjiPoFilmu(lista)
    elif odabrano == "3":
        pronadjiPoZanru(lista)
    elif odabrano == "4":
        pronadjiPoSali(lista)
    else:
        print("Pogresan unos")


def brisanjeProjekcije():
    """
    funkcija sluzi za logicko brisanje projekcija
    """
    lista = ucitavanje.projekcije
    ispisiTabelu(izbaciObrisane(lista))
    print()
    sifra = input("Unesi sifru projekcije koju zelis da obrises: ")
    flagNasao = True
    for i in range(len(lista)):
        if lista[i]["ID"] == sifra and lista[i]["Obrisano logicki"] == False:
            flagNasao = False
            lista[i]["Obrisano logicki"] = True
            ucitavanje.snimiSveProjekcije()
            print("Projekcija sa sifrom " + sifra + " uspesno obrisana")
    if flagNasao:
        print("Pogresna sifra za projekciju ")


def unesiNoviFilm():
    """
    funkcija sluzi za unos novog filma
    """
    sifraFilma = input("Unesite sifru filma: ")
    while len(sifraFilma) == 0 or daLiPostojiID(sifraFilma):
        print("Pogresan unos id probajte opet")
        sifraFilma = input("Unesite sifru filma: ")
    naziv = input("Unesite naziv filma: ")
    while len(naziv) == 0:
        print("Los unos, probajte opet ")
        naziv = input("Unesite naziv filma: ")
    zanr = ""
    while True:
        ispisiTabelu(ucitavanje.zanrovi)
        opcija = input("Unesite zanr koji zelite: ")
        if opcija == "1":
            zanr = "Akcioni"
            break
        elif opcija == "2":
            zanr = "Deciji"
            break
        elif opcija == "3":
            zanr = "Horor"
            break
        elif opcija == "4":
            zanr = "Romanticni"
            break
        else:
            print("Los Unos")

    ucitavanje.filmovi.append({"ID": sifraFilma, "Naziv": naziv, "Zanr": zanr})
    ucitavanje.snimiFilmove()
    return sifraFilma


def daLiPostojiID(idFilma):
    """
    funkcija sluzi za proveru da li postoji uneti idFilma
    """
    filmovi = ucitavanje.filmovi
    for i in range(len(filmovi)):
        if filmovi[i]["ID"] == idFilma:
            return True
    return False


def pretvoriMinute(vreme):
    """
    funkcija sluzi za konverziju vremena u minute
    """
    t = vreme.split(":")
    return int(t[0]) * 60 + int(t[1])


def preklapajuDvaTermina(pocetakPrvog, krajPrvog, pocetakDrugog, krajDrugog):
    """
    funkcija sluzi za proveru preklapanja dva termina
    """
    if pocetakDrugog < krajPrvog and pocetakPrvog < krajDrugog:
        return True
    return False


def unosNoveProjekcije():
    """
    funkcija sluzi za unos nove projekcije
    """
    id = input("Unesi ID projekcije: ")
    while postojiIDProjekcije(id):
        print("Uneti ID vec postoji, unesti drugi")
        id = input("Unesi ID projekcije: ")

    sala = input("Unesite salu: ")
    while len(sala) == 0:
        print("Los unos")
        sala = input("Unesite salu: ")

    datum = input("Unesi datum u formatu (D.M.G.)")
    while losDatum(datum):
        print("Los unos datuma")
        datum = input("Unesi datum u formatu (D.M.G.)")

    trajanjePr = input("Unesi trajanje projekcije u minutima: ")
    while loseTrajanje(trajanjePr):
        print("Los unos trajanja projekcije")
        trajanjePr = input("Unesi trajanje projekcije u minutima: ")
    vremePocetka = ""
    while True:
        vremePocetka = input("Unesi vreme pocetka u formatu (S:M)")
        while losPocetak(vremePocetka):
            print("Los unos vremena pocetka")
            vremePocetka = input("Unesi vreme pocetka u formatu (S:M)")
        pocetakUnete = pretvoriMinute(vremePocetka)
        krajUnete = pocetakUnete + int(trajanjePr)
        konflikt = False
        for i in ucitavanje.projekcije:
            if i["ID Sale"] == sala and i["Datum pocetka"] == datum:
                pocetakTrenutne = pretvoriMinute(i["Vreme pocetka"])
                krajTrenutne = pocetakTrenutne + i["Trajanje"]
                if preklapajuDvaTermina(pocetakUnete, krajUnete, pocetakTrenutne, krajTrenutne):
                    konflikt = True
        if konflikt:
            print("Preklapanje termina")
        else:
            break

    cena = input("Unesi cenu karte za projekciju: ")
    while losaCena(cena):
        print("Los unos cene projekcije")
        cena = input("Unesi cenu karte za projekciju: ")

    print("Da li zelite unos novog filma ili postojeceg ?")
    flag = True
    idFilma = ""
    while flag:
        print("1) Novi film: ")
        print("2) Postojeci: ")
        opcija = input(">> ")
        if opcija == "1":
            idFilma = unesiNoviFilm()  ####### NAPRAVI OVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
            flag = False
        elif opcija == "2":
            trajanje = True
            while trajanje:
                ispisiTabelu(ucitavanje.filmovi)
                idFilma = input("Unesti id od ponudjenih: ")
                trajanje = not (daLiPostojiID(idFilma))
                if trajanje:
                    print("Ne postoji taj id, probajte ponovo: ")
            flag = False
        else:
            print("Los unos pokusajte ponovo: ")

    ukupnoMesta = ""
    while True:
        ukupnoMesta = input("Unesite ukupno mesta za projekciju: ")
        try:
            if int(ukupnoMesta) <= 0:
                print("Los unos")
                continue
            break
        except ValueError:
            print("Los unos")
            continue

    ucitavanje.projekcije.append(
        {"ID": id, "Datum pocetka": datum, "Vreme pocetka": vremePocetka, "Trajanje": trajanjePr, "Cena": cena,
         "Film": idFilma, "ID Sale": sala, "Slobodna mesta": int(ukupnoMesta), "Ukupno mesta": int(ukupnoMesta),
         "Obrisano logicki": False})
    ucitavanje.snimiSveProjekcije()


def postojiIDProjekcije(id):
    """
    funkcija sluzi za proveru postojanja projekcije sa unetim id
    """
    lista = ucitavanje.projekcije
    for i in range(len(lista)):
        if lista[i]["ID"] == id:
            return True
    return False


def losDatum(date_text):
    """
    funkcija sluzi za proveru ispravnosti formata unetog datuma
    """
    try:
        datetime.datetime.strptime(date_text, '%d.%m.%Y.')
    except ValueError:
        return True
    return False


def losPocetak(vremePocetka):
    """
    funkcija sluzi za proveru ispravnosti unetog vremena
    """
    try:
        L = vremePocetka.split(":")
        if len(L) != 2:
            return True
        sati = int(L[0])
        minuti = int(L[1])
        if (sati < 0 or sati > 23) or (minuti < 0 or minuti > 59):
            return True
    except ValueError:
        return True
    return False


def loseTrajanje(trajanje):
    """
    funkcija sluzi za proveru ispravnosti unetog trajanja projekcije
    """
    try:
        minuti = int(trajanje)
        if minuti < 0 or minuti > 360:
            return True
    except ValueError:
        return True
    return False


def losaCena(cena):
    """
    funkcija sluzi za proveru ispravnosti unete cene projekcije
    """
    try:
        c = int(cena)
        if c < 0:
            return True
    except ValueError:
        return True
    return False


def meniIzmena():
    """
    funkcija sluzi za prikaz menija kod izmene projekcije
    """
    print("1) Datum projekcije")
    print("2) Vreme pocetka")
    print("3) Trajanje")
    print("4) Cena")
    print("5) Film")
    print("6) Sala")
    print("7) Slobodna sedista")
    print("8) Ukupno sedista")


def izmenaProjekcije():
    """
    funkcija sluzi za menjaje atributa odabrane projekcije
    """
    ispisiTabelu(izbaciObrisane(ucitavanje.projekcije))

    while True:
        sifra = input("Unesite sifru projekcije: ")
        while len(sifra.strip()) == 0:
            print("Los unos")
            sifra = input("Unesite sifru projekcije: ")
        for i in range(len(ucitavanje.projekcije)):
            if ucitavanje.projekcije[i]["ID"] == sifra:
                meniIzmena()
                opcija = input(">> ")
                if opcija == "1":
                    datum = input("Unesi datum u formatu (D.M.G.)")
                    while losDatum(datum):
                        print("Los unos datuma")
                        datum = input("Unesi datum u formatu (D.M.G.)")
                    ucitavanje.projekcije[i]["Datum pocetka"] = datum
                elif opcija == "2":
                    vremePocetka = input("Unesi vreme pocetka u formatu (S:M)")
                    while losPocetak(vremePocetka):
                        print("Los unos vremena pocetka")
                        vremePocetka = input("Unesi vreme pocetka u formatu (S:M)")
                    ucitavanje.projekcije[i]["Vreme pocetka"] = vremePocetka
                elif opcija == "3":
                    trajanjePr = input("Unesi trajanje projekcije u minutima: ")
                    while loseTrajanje(trajanjePr):
                        print("Los unos trajanja projekcije")
                        trajanjePr = input("Unesi trajanje projekcije u minutima: ")
                    ucitavanje.projekcije[i]["Trajanje"] = trajanjePr
                elif opcija == "4":
                    cena = input("Unesi cenu karte za projekciju: ")
                    while losaCena(cena):
                        print("Los unos cene projekcije")
                        cena = input("Unesi cenu karte za projekciju: ")
                    ucitavanje.projekcije[i]["Cena"] = cena
                elif opcija == "5":
                    idFilma = ""
                    while True:
                        ispisiTabelu(ucitavanje.filmovi)
                        idFilma = input("Unesti id od ponudjenih: ")
                        trajanje = not (daLiPostojiID(idFilma))
                        if trajanje:
                            print("Ne postoji taj id, probajte ponovo: ")
                        else:
                            break
                    ucitavanje.projekcije[i]["Film"] = idFilma
                elif opcija == "6":
                    sala = input("Unesite salu: ")
                    while len(sala) == 0:
                        print("Los unos")
                        sala = input("Unesite salu: ")
                    ucitavanje.projekcije[i]["ID Sale"] = sala
                elif opcija == "7":
                    slobodnaMesta = ""
                    while True:
                        slobodnaMesta = input("Unesite ukupno mesta za projekciju: ")
                        try:
                            if int(slobodnaMesta) <= 0:
                                print("Los unos")
                                continue

                            if ucitavanje.projekcije[i]["Ukupno mesta"] < int(slobodnaMesta):
                                print("Los unos, jer projekcija ima " + str(
                                    ucitavanje.projekcije[i]["Ukupno mesta"]) + " mesta ukupno")
                                continue
                            break
                        except ValueError:
                            print("Los unos")
                            continue
                    ucitavanje.projekcije[i]["Slobodna mesta"] = int(slobodnaMesta)
                elif opcija == "8":
                    ukupnoMesta = ""
                    while True:
                        ukupnoMesta = input("Unesite ukupno mesta za projekciju: ")
                        try:
                            if int(ukupnoMesta) <= 0:
                                print("Los unos")
                                continue
                            if ucitavanje.projekcije[i]["Slobodna mesta"] > int(ukupnoMesta):
                                print("Los unos, jer projekcija ima " + str(
                                    ucitavanje.projekcije[i]["Slobodna mesta"]) + " slobodna mesta")
                                continue
                            break
                        except ValueError:
                            print("Los unos")
                            continue
                    ucitavanje.projekcije[i]["Ukupno mesta"] = int(ukupnoMesta)
                else:
                    print("Los unos")
                    return

        ucitavanje.snimiSveProjekcije()
        break


def opcije():
    """
    funkcija sluzi za osvnovni meni kod menadzera
    """
    while True:
        ispisiMain()
        odabrano = input(">> ")
        if odabrano == "1":
            pretragaProjekcija()
        elif odabrano == "2":
            unosNoveProjekcije()
        elif odabrano == "3":
            brisanjeProjekcije()
        elif odabrano == "4":
            izmenaProjekcije()
        elif odabrano == "5":
            break
        else:
            print("Los unos, pokusajte ponovo")
            print()
