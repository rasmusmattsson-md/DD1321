# main.py
from meny import visa_meny
from order import gora_bestallning
from sallader import visa_alla_sallader, lagg_till_sallad, las_sallader, las_ingredienser, spara_sallader

def main():
    sallader = las_sallader()
    ingredienser = las_ingredienser()
    
    while True:
        visa_meny()
        val = input("\nVälj alternativ: ").strip()
        
        if val == "1":
            visa_alla_sallader(sallader)
        elif val == "2":
            gora_bestallning(sallader, ingredienser)
        elif val == "3":
            lagg_till_sallad(sallader, ingredienser)
        elif val == "4":
            spara_sallader(sallader)
            print("Programmet avslutas. Alla ändringar sparade!")
            break
        else:
            print("Ogiltigt val!")

if __name__ == "__main__":
    main()
