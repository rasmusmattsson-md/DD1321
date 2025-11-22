class Person:
    def __init__(self, namn, personnummer):
        self.namn = namn
        self.personnummer = personnummer
        self.husdjur = []
        self.epost = ""
        self.mobil = ""
        self.ålder = 0

    def add_pet(self, typ, namn, ras):
        self.husdjur.append({
            "typ": typ,
            "namn": namn,
            "ras": ras
        })
