# order_gui.py (replace order.py content)

def hitta_ingrediens_pris(ingredienser, namn):
    for ing in ingredienser:
        if ing["namn"] == namn:
            return ing["pris"]
    return 0.0

def rakna_matchningar(sallad_ingredienser, kund_ingredienser):
    return sum(1 for ing in kund_ingredienser if ing in sallad_ingredienser)

def hitta_basta_match(sallader, kund_ingredienser):
    bast_index = 0
    bast_match = 0
    for i, sallad in enumerate(sallader):
        m = rakna_matchningar(sallad["ingredienser"], kund_ingredienser)
        if m > bast_match:
            bast_match = m
            bast_index = i
    return bast_index

def gora_bestallning(sallader, ingredienser, gui_input, gui_alert, log):
    log("--- GÖR EN BESTÄLLNING ---")

    val = gui_input("Vill du beställa en färdig sallad från menyn? (j/n):")
    if val is None:
        return

    if val.lower() == "j":
        lista = [f"{i+1}. {s['namn']} - {s['pris']:.2f} kr" for i, s in enumerate(sallader)]
        gui_alert("Färdiga sallader:\n" + "\n".join(lista))

        nummer = gui_input("Välj nummer:")
        if nummer is None:
            return

        try:
            nummer = int(nummer) - 1
        except:
            gui_alert("Ogiltigt nummer.")
            return

        if 0 <= nummer < len(sallader):
            s = sallader[nummer]
            gui_alert(f"Du har beställt: {s['namn']}\nPris: {s['pris']:.2f} kr")
        else:
            gui_alert("Ogiltigt val.")
        return

    # Skapa egen sallad
    gui_alert("Skapa egen sallad.")

    ing_lista = [ing["namn"] for ing in ingredienser]
    gui_alert("Tillgängliga ingredienser:\n" + "\n".join(ing_lista))

    ing_text = gui_input("Ange ingredienser (komma-separerat):")
    if ing_text is None:
        return

    kund_ingredienser = [i.strip() for i in ing_text.split(",")]

    bast_index = hitta_basta_match(sallader, kund_ingredienser)
    bast_sallad = sallader[bast_index]

    # Perfekt match
    if set(kund_ingredienser) == set(bast_sallad["ingredienser"]):
        gui_alert(
            f"Perfekt match! '{bast_sallad['namn']}' matchar exakt!\n"
            f"Pris: {bast_sallad['pris']:.2f} kr"
        )
        return

    # Anpassning
    gui_alert(f"Vi utgår från '{bast_sallad['namn']}' och anpassar den.")
    nytt_pris = bast_sallad["pris"]
    grundkostnad = 30.0

    # ta bort
    for ing in bast_sallad["ingredienser"]:
        if ing not in kund_ingredienser:
            pris = hitta_ingrediens_pris(ingredienser, ing)
            nytt_pris -= pris
            log(f"Tar bort: {ing} (-{pris:.2f} kr)")

    # lägg till
    for ing in kund_ingredienser:
        if ing not in bast_sallad["ingredienser"]:
            pris = hitta_ingrediens_pris(ingredienser, ing)
            nytt_pris += pris
            log(f"Lägger till: {ing} (+{pris:.2f} kr)")

    if nytt_pris < grundkostnad:
        nytt_pris = grundkostnad

    gui_alert(f"Slutpris: {nytt_pris:.2f} kr")
