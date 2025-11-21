
import sys


# # Läs in från fil
def readFile(filnamn):
    ord_lista = []
    
    with open(filnamn, 'r') as filen:
        for rad in filen:
            ord = rad.strip()
            ord_lista.append(ord)
    
    return ord_lista

# Main-funktion
def main():
    # Kolla om användaren angett ett lösenord som argument
    if len(sys.argv) > 1:
        word_to_test = sys.argv[1]
    else:
        print("Kör programmet så här\n\tpython3", sys.argv[0], "<ord>")
        sys.exit()
    
    # Läs in alla dåliga lösenordsvarianter
    dåliga_lösenord = readFile("all_passwords.txt")
    
    # Kolla om lösenordet finns i listan
    if word_to_test in dåliga_lösenord:
        print(f"❌ VARNING! '{word_to_test}' är INTE ett säkert lösenord!")
        print("Detta lösenord är lätt att gissa. Välj ett annat.")
    else:
        print(f"✓ '{word_to_test}' verkar vara ett OK lösenord!")
        print("Det finns inte i listan över vanliga lösenordsvarianter.")


main()