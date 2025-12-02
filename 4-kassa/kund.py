
# ============================================================
# kund.py
from varulager import hitta_vara
from kvitto import skriv_kvitto

def ny_kund(varor):
    """Hanterar ny kund och skapar kvitto"""
    korg = []
    
    print("\n--- NY KUND ---")
    print("Ange artikelnummer (tom rad för att avsluta)")
    
    while True:
        artikelnr = input("Artikelnummer: ").strip()
        if artikelnr == "":
            break
            
        index = hitta_vara(varor, artikelnr)
        if index == -1:
            print("Varan finns inte!")
            continue
        
        vara = varor[index]
        antal = int(input("Antal: "))
        
        # Kolla lagersaldo
        if antal > vara["antal"]:
            print(f"Endast {vara['antal']} st finns i lager!")
            antal = vara["antal"]
        
        if antal > 0:
            # Minska lagersaldo
            varor[index]["antal"] -= antal
            
            # Kolla om varan redan finns i korgen
            hittad = False
            for i in range(len(korg)):
                if korg[i]["artikelnr"] == artikelnr:
                    korg[i]["antal"] += antal
                    hittad = True
                    break
            
            if not hittad:
                korg.append({
                    "namn": vara["namn"],
                    "artikelnr": vara["artikelnr"],
                    "pris": vara["pris"],
                    "antal": antal
                })
            
            print(f"{antal} st {vara['namn']} tillagd")
    
    # Möjlighet att ångra vara
    while True:
        angra = input("\nVill du ångra någon vara? (j/n): ").lower()
        if angra != "j":
            break
        
        artikelnr = input("Artikelnummer att ångra: ").strip()
        for i in range(len(korg)):
            if korg[i]["artikelnr"] == artikelnr:
                antal_angra = int(input(f"Antal att ångra (max {korg[i]['antal']}): "))
                if antal_angra >= korg[i]["antal"]:
                    antal_angra = korg[i]["antal"]
                    korg.pop(i)
                else:
                    korg[i]["antal"] -= antal_angra
                
                # Återställ lagersaldo
                index = hitta_vara(varor, artikelnr)
                varor[index]["antal"] += antal_angra
                print(f"{antal_angra} st borttaget")
                break
        else:
            print("Varan finns inte i korgen!")
    
    # Skriv ut kvitto
    if len(korg) > 0:
        skriv_kvitto(korg)

def lamna_tillbaka(varor):
    """Hantera returvaror"""
    print("\n--- LÄMNA TILLBAKA VARA ---")
    artikelnr = input("Artikelnummer: ").strip()
    
    index = hitta_vara(varor, artikelnr)
    if index == -1:
        print("Varan finns inte!")
        return
    
    antal = int(input("Antal att lämna tillbaka: "))
    varor[index]["antal"] += antal
    
    aterbetalning = varor[index]["pris"] * antal
    print(f"Återbetalning: {aterbetalning:.2f} kr")
    print(f"Lagersaldo uppdaterat till {varor[index]['antal']} st")
