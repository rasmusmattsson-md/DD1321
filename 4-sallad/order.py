
# ============================================================
# bestallning.py
def hitta_ingrediens_pris(ingredienser, namn):
    """Hittar pris för en ingrediens"""
    for ing in ingredienser:
        if ing["namn"] == namn:
            return ing["pris"]
    return 0.0

def rakna_matchningar(sallad_ingredienser, kund_ingredienser):
    """Räknar hur många ingredienser som matchar"""
    matchningar = 0
    for ing in kund_ingredienser:
        if ing in sallad_ingredienser:
            matchningar += 1
    return matchningar

def hitta_basta_match(sallader, kund_ingredienser):
    """Hittar salladen som matchar bäst med kundens val"""
    bast_index = 0
    bast_matchningar = 0
    
    for i in range(len(sallader)):
        matchningar = rakna_matchningar(sallader[i]["ingredienser"], kund_ingredienser)
        if matchningar > bast_matchningar:
            bast_matchningar = matchningar
            bast_index = i
    
    return bast_index

def gora_bestallning(sallader, ingredienser):
    """Hantera en beställning"""
    print("\n--- GÖR EN BESTÄLLNING ---")
    
    val = input("Vill du beställa en färdig sallad från menyn? (j/n): ").lower()
    
    if val == "j":
        print("\nFärdiga sallader:")
        for i, sallad in enumerate(sallader, 1):
            print(f"{i}. {sallad['namn']} - {sallad['pris']:.2f} kr")
        
        nummer = int(input("\nVälj nummer: ")) - 1
        if 0 <= nummer < len(sallader):
            vald_sallad = sallader[nummer]
            print(f"\nDu har beställt: {vald_sallad['namn']}")
            print(f"Pris: {vald_sallad['pris']:.2f} kr")
        else:
            print("Ogiltigt val!")
    else:
        print("\nSkapa din egen sallad!")
        print("\nTillgängliga ingredienser:")
        for ing in ingredienser:
            print(f"  - {ing['namn']}")
        
        print("\nAnge ingredienser (separera med komma):")
        ing_text = input("Ingredienser: ")
        kund_ingredienser = [i.strip() for i in ing_text.split(",")]
        
        # Hitta bästa matchning
        bast_index = hitta_basta_match(sallader, kund_ingredienser)
        bast_sallad = sallader[bast_index]
        
        # Kolla om perfekt match
        if set(kund_ingredienser) == set(bast_sallad["ingredienser"]):
            print(f"\nPerfekt match! Vi har '{bast_sallad['namn']}' som matchar exakt!")
            print(f"Pris: {bast_sallad['pris']:.2f} kr")
        else:
            print(f"\nVi utgår från '{bast_sallad['namn']}' och anpassar den!")
            
            # Beräkna nytt pris
            nytt_pris = bast_sallad["pris"]
            grundkostnad = 30.0
            
            # Ta bort ingredienser som inte önskas
            for ing in bast_sallad["ingredienser"]:
                if ing not in kund_ingredienser:
                    pris = hitta_ingrediens_pris(ingredienser, ing)
                    nytt_pris -= pris
                    print(f"  Tar bort: {ing} (-{pris:.2f} kr)")
            
            # Lägg till nya ingredienser
            for ing in kund_ingredienser:
                if ing not in bast_sallad["ingredienser"]:
                    pris = hitta_ingrediens_pris(ingredienser, ing)
                    nytt_pris += pris
                    print(f"  Lägger till: {ing} (+{pris:.2f} kr)")
            
            # Se till att priset inte blir negativt
            if nytt_pris < grundkostnad:
                nytt_pris = grundkostnad
            
            print(f"\nSlutpris: {nytt_pris:.2f} kr")

