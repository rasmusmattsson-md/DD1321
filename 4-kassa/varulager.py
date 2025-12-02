# ============================================================
# varulager.py
import json

def las_varor():
    try:
        with open("varor.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("Ingen varufil hittades. Skapar testdata...")
        varor = [
            {"namn": "Harpa", "artikelnr": "1001", "pris": 50000.0, "antal": 5},
            {"namn": "Mjölk", "artikelnr": "2001", "pris": 15.50, "antal": 20},
            {"namn": "Bröd", "artikelnr": "2002", "pris": 25.0, "antal": 15}
        ]
        spara_varor(varor)
        return varor

def spara_varor(varor):
    with open("varor.json", "w", encoding="utf-8") as f:
        json.dump(varor, f, ensure_ascii=False, indent=2)

def hitta_vara(varor, artikelnr):
    """Hittar vara med artikelnummer, returnerar index eller -1"""
    for i in range(len(varor)):
        if varor[i]["artikelnr"] == artikelnr:
            return i
    return -1

def skapa_vara():
    alla_varor = las_varor()
    if not isinstance(alla_varor, list):
        alla_varor = []

    namn = input("Ange namn: ")
    artikelnummer = input("Ange artikelnummer: ")
    pris = float(input("Ange styckpris: "))

    vara = {
        "namn": namn,
        "artikelnr": artikelnummer,
        "pris": pris,
        "antal": 0,
    }

    alla_varor.append(vara)

    with open("varor.json", "w", encoding="utf-8") as f:
        json.dump(alla_varor, f, ensure_ascii=False, indent=2)

    return vara

def uppdatera_varuutbud(varor):
    """Hantera varuutbudet"""
    print("\n--- UPPDATERA VARUUTBUD ---")
    print("1. Lägg till vara")
    print("2. Uppdatera lagersaldo")
    print("3. Ta bort vara")
    
    val = input("Välj: ").strip()
    
    if val == "1":
        namn = input("Varunamn: ")
        artikelnr = input("Artikelnummer: ")
        pris = float(input("Pris: "))
        antal = int(input("Antal: "))
        varor.append({"namn": namn, "artikelnr": artikelnr, "pris": pris, "antal": antal})
        print("Vara tillagd!")
    
    elif val == "2":
        artikelnr = input("Artikelnummer: ").strip()
        index = hitta_vara(varor, artikelnr)
        if index == -1:
            print("Varan finns inte!")
        else:
            nytt_antal = int(input("Nytt lagersaldo: "))
            varor[index]["antal"] = nytt_antal
            print("Lagersaldo uppdaterat!")
    
    elif val == "3":
        artikelnr = input("Artikelnummer: ").strip()
        index = hitta_vara(varor, artikelnr)
        if index == -1:
            print("Varan finns inte!")
        else:
            varor.pop(index)
            print("Vara borttagen!")
