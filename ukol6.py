class Auto:
    def __int__ (self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = True

    def pujc_auto(self):
        if self.dostupnost:
            self.dostupnost = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"

    def get_info(self):
        return f"Auto {self.typ_vozidla}, reg. značka {self.registracni_znacka}"
    
Auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Auto2 = Auto("1P3 4747", "Skoda Octavia", 41253)


výber_auta = input("Jake auto si prejete pujcit?")

if výber_auta == "Auto1":
    print(Auto1.pujc_auto())
elif výber_auta == "Auto2":
    print(Auto2.pujc_auto())
else:
    print(f"Model '{výber_auta}' neni k dispozici.K dispozici jsou modely: Peugeot a Škoda")

