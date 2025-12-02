# main.py
from meny import visa_meny
from kund import ny_kund, lamna_tillbaka
from varulager import uppdatera_varuutbud, las_varor, spara_varor, skapa_vara

def main():
    varor = las_varor()
    
    while True:
        visa_meny()
        val = input("\nVälj alternativ: ").strip()
        if val == "1":
            ny_kund(varor)
        elif val == "2":
            lamna_tillbaka(varor)
        elif val == "3":
            skapa_vara()
        elif val == "4":
            uppdatera_varuutbud(varor)
        elif val == "5":
            spara_varor(varor)
            print("Programmet avslutas. Alla ändringar sparade!")
            break
        else:
            print("Ogiltigt val!")

if __name__ == "__main__":
    main()

