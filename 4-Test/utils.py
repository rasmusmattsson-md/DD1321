import json


def show_menu():
    print("\n=== TELEFONBOKEN ===")
    print("1. Lägga till nya kontakter")
    print("2. Ta bort kontakter")
    print("3. Uppdatera befintliga kontakter")
    print("4. Visa alla kontakter inom en kontaktgrupp")
    print("5. Öppna en kontakt")
    print("6. Avsluta")
    return input("\nVälj ett alternativ (1-6): ")

def load_contacts():
    """Ladda kontakter från contacts.json"""
    try:
        with open("contacts.json", "r", encoding="utf-8") as f:
            contacts = json.load(f)
        print(f"Laddade {len(contacts)} kontakter")
        return contacts
    except FileNotFoundError:
        print("Ingen kontaktfil hittades. Startar med tom telefonbok.")
        return []

def save_contacts(contacts):
    """Spara kontakter till contacts.json"""
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
    print("Kontakter sparade!")

def add_contact(contacts):
    """Lägg till en ny kontakt"""
    print("\n--- Lägg till ny kontakt ---")
    first_name = input("Förnamn: ")
    last_name = input("Efternamn: ")
    phone = input("Telefonnummer: ")
    email = input("Email: ")
    birthday = input("Födelsedag (YYYY-MM-DD): ")
    group = input("Kontaktgrupp (tex. familjen): ")
    
    contact = {
        "förnamn": first_name,
        "efternamn": last_name,
        "telefonnummer": phone,
        "email": email,
        "födelsedag": birthday,
        "kontaktgrupp": group,
        "anteckningar": []
    }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"✓ Kontakt {first_name} {last_name} har lagts till!")

def remove_contact(contacts):
    """Ta bort en kontakt"""
    print("\n--- Ta bort kontakt ---")
    name = input("Skriv namn på kontakt att ta bort: ")
    for c in contacts:
        if name.lower() in (c["förnamn"] + " " + c["efternamn"]).lower():
            contacts.remove(c)
            save_contacts(contacts)
            print(f"✓ Kontakt {name} har tagits bort!")
            return
    print("✗ Kontakt hittades inte.")

def update_contact(contacts):
    """Uppdatera en befintlig kontakt"""
    print("\n--- Uppdatera kontakt ---")
    name = input("Skriv namn på kontakt att uppdatera: ")
    for c in contacts:
        if name.lower() in (c["förnamn"] + " " + c["efternamn"]).lower():
            print("\nVad vill du uppdatera?")
            print("1. Telefonnummer")
            print("2. Email")
            print("3. Födelsedag")
            print("4. Kontaktgrupp")
            choice = input("Välj (1-4): ")
            
            if choice == "1":
                c["telefonnummer"] = input("Nytt telefonnummer: ")
            elif choice == "2":
                c["email"] = input("Ny email: ")
            elif choice == "3":
                c["födelsedag"] = input("Ny födelsedag: ")
            elif choice == "4":
                c["kontaktgrupp"] = input("Ny kontaktgrupp: ")
            save_contacts(contacts)
            print("✓ Kontakt uppdaterad!")
            return
    print("✗ Kontakt hittades inte.")