class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.occupants = []

    def add_occupant(self, person):
        self.occupants.append(person)
        person.location = self

    def remove_occupant(self, person):
        self.occupants.remove(person)
        person.location = None