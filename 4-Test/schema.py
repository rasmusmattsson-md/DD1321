class Contact:
    def __init__(self, first_name, last_name, phone, email, birthday, group, notes=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.birthday = birthday
        self.group = group
        self.notes = notes or []

    def to_dict(self):
        return {
            "förnamn": self.first_name,
            "efternamn": self.last_name,
            "telefonnummer": self.phone,
            "email": self.email,
            "födelsedag": self.birthday,
            "kontaktgrupp": self.group,
            "anteckningar": self.notes
        }

    @staticmethod
    def from_dict(d):
        return Contact(
            d["förnamn"],
            d["efternamn"],
            d["telefonnummer"],
            d["email"],
            d["födelsedag"],
            d["kontaktgrupp"],
            d.get("anteckningar", [])
        )
