from dataclasses import dataclass


@dataclass
class Airport:
    id: int
    name: str
    iata: str
    city: str

    def __str__(self):
        return f'{self.iata} - {self.city}'

    def __hash__(self):
        return hash(self.id)
