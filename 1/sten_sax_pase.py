# Program: Labb 1 - Sten, Sax, Påse
# Kurs: DD1321
# Skapare: Rasmus Mattsson
# Datum: 2025-11-21
# Beskrivning: Ett spel där användaren tävlar mot datorn i sten, sax, påse.
#              Bäst av tre rundor vinner!

import random

# Dictionary med vinstregler
vinst_dictionary = {
    'sten': 'sax',
    'sax': 'påse',
    'påse': 'sten'
}

# Lista med valalternativ
valalternativ_lista = ['sten', 'sax', 'påse']

# Store points
spelar_poang = 0
dator_poang = 0

# Game-loop. Continue until either gets 2 points
while spelar_poang < 2 and dator_poang < 2:
    # Låt användaren välja
    print("\nVälj mellan: sten, sax eller påse")
    användar_val = input("Ditt val: ")
    
    # Låt datorn välja slumpmässigt
    slump_index = random.randint(0, 2)
    dator_val = valalternativ_lista[slump_index]
    print(f"Datorn valde: {dator_val}")
    
    # Kolla vem som vann
    if användar_val == dator_val:
        print("Oavgjort!")
    elif vinst_dictionary[dator_val] == användar_val:
        dator_poang = dator_poang + 1
        print("Datorn vinner denna runda!")
    else:
        spelar_poang = spelar_poang + 1
        print("Du vinner denna runda!")
    
    # Skriv ut poängställning
    print(f"Poäng - Du: {spelar_poang}, Datorn: {dator_poang}")

# Skriv ut slutgiltig vinnare
print("\n--- SPELET SLUT ---")
if spelar_poang > dator_poang:
    print("GRATTIS! Du vann hela spelet!")
else:
    print("Datorn vann hela spelet. Bättre lycka nästa gång!")