from utils import load_contacts, save_contacts, add_contact, remove_contact, update_contact, show_menu

contacts = []

def show_group():
    print("\n--- Visa kontaktgrupp ---")
    group = input("Skriv kontaktgrupp: ")
    found = False
    for c in contacts:
        if c["kontaktgrupp"].lower() == group.lower():
            print(f"\n{c['förnamn']} {c['efternamn']}")
            print(f"  Tel: {c['telefonnummer']}")
            print(f"  Email: {c['email']}")
            found = True
    if not found:
        print("Inga kontakter i denna grupp.")

def open_contact():
    print("\n--- Öppna kontakt ---")
    name = input("Skriv namn på kontakt: ")
    for c in contacts:
        if name.lower() in (c["förnamn"] + " " + c["efternamn"]).lower():
            print(f"\n=== {c['förnamn']} {c['efternamn']} ===")
            print(f"Telefon: {c['telefonnummer']}")
            print(f"Email: {c['email']}")
            print(f"Födelsedag: {c['födelsedag']}")
            print(f"Kontaktgrupp: {c['kontaktgrupp']}")
            print(f"\nAnteckningar ({len(c['anteckningar'])} st):")
            for i, note in enumerate(c['anteckningar'], 1):
                print(f"  {i}. {note['titel']} ({note['datum']})")
            
            print("\n1. Skriv en ny anteckning")
            print("2. Läs alla gamla anteckningar")
            print("3. Tillbaka")
            choice = input("Välj: ")
            
            if choice == "1":
                title = input("Titel: ")
                date = input("Datum: ")
                note_text = input("Anteckning: ")
                c['anteckningar'].append({
                    "titel": title,
                    "datum": date,
                    "anteckning": note_text
                })
                save_contacts(contacts)
                print("✓ Anteckning sparad!")
            elif choice == "2":
                for note in c['anteckningar']:
                    print(f"\n--- {note['titel']} ({note['datum']}) ---")
                    print(note['anteckning'])
            return
    print("✗ Kontakt hittades inte.")

def main():
    global contacts
    contacts = load_contacts()
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            remove_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            show_group()
        elif choice == "5":
            open_contact()
        elif choice == "6":
            print("\nHej då!")
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()