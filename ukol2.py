sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10}

kod_soucastky = input("Zadejte kód součástky: ")
mnozstvi = int(input("Zadejte množství: "))

if kod_soucastky not in sklad:
    print(f"Soucastka {kod_soucastky} neni skladem.")
else:
    if sklad[kod_soucastky] < mnozstvi:
        print(f"Soucastky {kod_soucastky} lze prodat jen omezene mnozstvi {sklad[kod_soucastky]} .")
        sklad.pop(kod_soucastky)
    else:
        print(f"Poptavku lze uspokojit v plne vysi.")
        sklad[kod_soucastky] -= mnozstvi

    
