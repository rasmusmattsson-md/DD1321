
# ============================================================
# sallader.py
import json

def las_sallader():
    """Läser sallader från JSON-fil"""
    try:
        with open("sallader.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("Ingen salladsfil hittades. Skapar testdata...")
        sallader = [
            {
                "namn": "Caesar",
                "pris": 89.0,
                "ingredienser": ["sallad", "kyckling", "parmesan", "krutonger", "caesardressing"]
            },
            {
                "namn": "Grekisk",
                "pris": 79.0,
                "ingredienser": ["sallad", "tomat", "gurka", "fetaost", "oliver", "rödlök"]
            },
            {
                "namn": "Tonfisk",
                "pris": 85.0,
                "ingredienser": ["sallad", "tonfisk", "tomat", "majs", "ägg"]
            }
        ]
        spara_sallader(sallader)
        return sallader

def las_ingredienser():
    """Läser ingredienser från JSON-fil"""
    try:
        with open("ingredienser.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("Ingen ingrediensfil hittades. Skapar testdata...")
        ingredienser = [
            {"namn": "sallad", "pris": 10.0},
            {"namn": "tomat", "pris": 8.0},
            {"namn": "gurka", "pris": 7.0},
            {"namn": "kyckling", "pris": 20.0},
            {"namn": "tonfisk", "pris": 18.0},
            {"namn": "fetaost", "pris": 15.0},
            {"namn": "parmesan", "pris": 12.0},
            {"namn": "ägg", "pris": 10.0},
            {"namn": "majs", "pris": 6.0},
            {"namn": "oliver", "pris": 9.0},
            {"namn": "rödlök", "pris": 5.0},
            {"namn": "krutonger", "pris": 8.0},
            {"namn": "caesardressing", "pris": 10.0}
        ]
        spara_ingredienser(ingredienser)
        return ingredienser

def spara_sallader(sallader):
    """Sparar sallader till JSON-fil"""
    with open("sallader.json", "w", encoding="utf-8") as f:
        json.dump(sallader, f, ensure_ascii=False, indent=2)

def spara_ingredienser(ingredienser):
    """Sparar ingredienser till JSON-fil"""
    with open("ingredienser.json", "w", encoding="utf-8") as f:
        json.dump(ingredienser, f, ensure_ascii=False, indent=2)

def visa_alla_sallader(sallader):
    """Visar alla sallader med priser och ingredienser"""
    print("\n" + "="*60)
    print("SALLADSCAFÉETS MENY".center(60))
    print("="*60)
    
    for sallad in sallader:
        print(f"\n{sallad['namn']:20} {sallad['pris']:.2f} kr")
        print(f"  Ingredienser: {', '.join(sallad['ingredienser'])}")
    
    print("="*60)

def lagg_till_sallad(sallader, ingredienser):
    """Lägg till en ny sallad i menyn"""
    print("\n--- LÄGG TILL NY SALLAD ---")
    namn = input("Salladens namn: ")
    
    print("\nTillgängliga ingredienser:")
    for ing in ingredienser:
        print(f"  - {ing['namn']} ({ing['pris']:.2f} kr)")
    
    print("\nAnge ingredienser (separera med komma):")
    ing_text = input("Ingredienser: ")
    valda_ingredienser = [i.strip() for i in ing_text.split(",")]
    
    # Beräkna pris (ingredienser + grundkostnad)
    grundkostnad = 30.0
    totalpris = grundkostnad
    for ing_namn in valda_ingredienser:
        for ing in ingredienser:
            if ing["namn"] == ing_namn:
                totalpris += ing["pris"]
                break
    
    sallader.append({
        "namn": namn,
        "pris": totalpris,
        "ingredienser": valda_ingredienser
    })
    
    print(f"\nSallad '{namn}' tillagd med pris {totalpris:.2f} kr!")

