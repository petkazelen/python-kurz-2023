#cast1

def over_telefonni_cislo(cislo = True):
    return len(cislo) == 9 or (len(cislo) == 13 and cislo[0:4] == "+420")

cislo = input("zadejte telefon: ")
print(over_telefonni_cislo(cislo))


#cast2

import math

def spocti_cenu_zpravy(zprava):
    cena = math.ceil(len(zprava) / 180) * 3
    return cena

zprava = "Ahoj Honzo"
print(spocti_cenu_zpravy(zprava))

