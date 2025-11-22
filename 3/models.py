class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id
        self.pets = []
        self.email = ""
        self.mobile = ""
        self.age = 0

    def add_pet(self, pet_type, name, breed):
        self.pets.append({
            "type": pet_type,
            "name": name,
            "breed": breed
        })
