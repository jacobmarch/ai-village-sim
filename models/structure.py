from models import Person

class Structure:
    def __init__(self, name: str, description: str, max_occupants: int, purpose: str, owner: Person = None):
        self.name = name
        self.description = description
        self.occupants = []
        self.max_occupants = max_occupants
        self.purpose = purpose
        self.owner = owner
        
    def add_occupant(self, person):
        self.occupants.append(person)
        person.location = self

    def remove_occupant(self, person):
        self.occupants.remove(person)
        person.location = None
