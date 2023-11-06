import re
#Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí neplatná data:

regularni_vyraz = re.compile(r"\d\d?[./] ?\d\d?[./] ?\d{4}")

#posta.txt

regularni_vyraz = re.compile(r"\d{3} \d{2}  ?(\w ?)+( \d+)?")

vstup = input("Zadejte PSC a mesto:")
hledani =  regularni_vyraz.fullmatch(vstup)

if hledani:
    print("Dakujeme za adresu")
else:
    print("Nesprávná adresa!")