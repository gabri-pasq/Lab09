from dataclasses import dataclass




@dataclass
class Flight:
    id: int
    airportP: int
    airportA: int
    distanza: int



    def __hash__(self):
        return hash(self.id)