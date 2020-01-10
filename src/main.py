import ucitavanje
import menadzer
import prodavac

if __name__ == '__main__':
    ucitavanje.ucitajEntitete()

    print("<<<<<<<<<< Dobrodosli >>>>>>>>>>")
    trajanje = True
    losiPodaci = True
    while trajanje:
        ime = input("Unesite korisnicko ime: ")
        sifra = input('Unesite sifru: ')
        korisnici = ucitavanje.korisnici
        for i in range(len(korisnici)):
            if korisnici[i]["Korisnicko ime"] == ime and korisnici[i]["Sifra"] == sifra:
                losiPodaci = False
                if korisnici[i]["Uloga"] == "prodavac":
                    print("Uspesna prijava kao prodavac: " + korisnici[i]["Ime"] + " " + korisnici[i]["Prezime"])
                    prodavac.opcije()
                    trajanje = False
                elif korisnici[i]["Uloga"] == "menadzer":
                    print("Uspesna prijava kao menadzer: " + korisnici[i]["Ime"] + " " + korisnici[i]["Prezime"])
                    menadzer.opcije()
                    trajanje = False
        if losiPodaci:
            print("Pogresni podaci, pokusajte ponovo")
            print()
    print("Izasli ste iz aplikacije")
