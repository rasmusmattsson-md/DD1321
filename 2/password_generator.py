
# # Uppgift 2: Konvertera till stor bokstav
def capitalLetter(bokstav):
    # Dictionary med små och stora bokstäver
    alfabet = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
        'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
        'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
        'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
        'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y',
        'z': 'Z', 'å': 'Å', 'ä': 'Ä', 'ö': 'Ö'
    }
    
    # Om bokstaven finns i dictionaryt, returnera stor bokstav
    if bokstav in alfabet:
        return alfabet[bokstav]
    else:
        return bokstav


# Uppgift 3: Lista med en stor bokstav
def uppercaseList(ord):
    resultat = []
    
    # Gå igenom varje position i ordet
    for i in range(len(ord)):
        # Skapa nytt ord med stor bokstav på position i
        nytt_ord = ord[:i] + capitalLetter(ord[i]) + ord[i+1:]
        resultat.append(nytt_ord)
    
    return resultat


# Uppgift 4: Lista med två stora bokstäver
def doubleUppercaseList(ord):
    resultat = []
    
    # Gå igenom alla kombinationer av två positioner
    for i in range(len(ord)):
        for j in range(i+1, len(ord)):
            # Skapa ord med stora bokstäver på position i och j
            nytt_ord = ""
            for k in range(len(ord)):
                if k == i or k == j:
                    nytt_ord = nytt_ord + capitalLetter(ord[k])
                else:
                    nytt_ord = nytt_ord + ord[k]
            resultat.append(nytt_ord)
    
    return resultat


# Uppgift 5: Lista med inskjutna specialtecken
def insertSpecialChars(ord):
    resultat = []
    
    # Lista med specialtecken och siffror
    tecken = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']
    
    # För varje specialtecken
    for tecken_val in tecken:
        # Skjut in på varje möjlig position (innan, mellan och efter bokstäver)
        for i in range(len(ord) + 1):
            nytt_ord = ord[:i] + tecken_val + ord[i:]
            resultat.append(nytt_ord)
    
    return resultat


# Uppgift 6: Kombinera alla varianter
def createMasterList(ord):
    resultat = []
    
    # 1. Lägg till originalordet
    resultat.append(ord)
    
    # 2. Lägg till originalordet med inskjutna specialtecken
    resultat = resultat + insertSpecialChars(ord)
    
    # 3. Lägg till varianter med en stor bokstav
    en_stor_lista = uppercaseList(ord)
    resultat = resultat + en_stor_lista
    
    # 4. Lägg till varianter med en stor bokstav OCH specialtecken
    for variant in en_stor_lista:
        resultat = resultat + insertSpecialChars(variant)
    
    # 5. Lägg till varianter med två stora bokstäver
    två_stora_lista = doubleUppercaseList(ord)
    resultat = resultat + två_stora_lista
    
    # 6. Lägg till varianter med två stora bokstäver OCH specialtecken
    for variant in två_stora_lista:
        resultat = resultat + insertSpecialChars(variant)
    
    return resultat


# Uppgift 7: Läs in från fil
def readFile(filnamn):
    ord_lista = []
    
    with open(filnamn, 'r') as filen:
        for rad in filen:
            ord = rad.strip()
            ord_lista.append(ord)
    
    return ord_lista


# Uppgift 8: Spara på fil
def saveToFile(filnamn, lösenordslista):
    with open(filnamn, 'w') as filen:
        for lösenord in lösenordslista:
            filen.write("%s\n" % lösenord)


# Main-funktion
def main():
    # Test uppgift 2
    print("Test uppgift 2:")
    bokstavstest = capitalLetter('a')
    print(bokstavstest)
    
    # Test uppgift 3
    print("\nTest uppgift 3:")
    v3 = uppercaseList("admin")
    print(v3)
    
    # Test uppgift 4
    print("\nTest uppgift 4:")
    v4 = doubleUppercaseList("admin")
    print(v4)
    
    # Test uppgift 5
    print("\nTest uppgift 5 (med bara 2, 3 och +):")
    v5 = insertSpecialChars("och")
    print(v5)
    
    # Test uppgift 6 (med mindre testmängd)
    print("\nTest uppgift 6 (med fyra):")
    v6 = createMasterList("fyra")
    v6.sort()
    print(v6)
    
    # Uppgift 7 och 8: Läs från fil och spara alla varianter
    print("\nSkapar lösenordsfil...")
    ord_från_fil = readFile("passwords.txt")
    
    all_passwords = []
    for ord in ord_från_fil:
        all_passwords = all_passwords + createMasterList(ord)
    
    saveToFile("all_passwords.txt", all_passwords)
    print(f"Färdig! Totalt {len(all_passwords)} lösenordsvarianter sparade i all_passwords.txt")


main()