from dataclasses import dataclass

@dataclass
class Player:
    id: str
    name: str
    surname: str
    salary : int

    def __hash__(self):
        return hash(self.id)
    def __str__(self):
        return f"ID={self.id}, NAME={self.name}, SURNAME={self.surname}"