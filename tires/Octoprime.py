from typing import List
from tire import Tire

class Octoprime(Tire):

    def __init__(self, tire_data:List[int]) -> None:
        self.tire_data = tire_data

    def needs_service(self) -> bool:
        
        return sum(self.tire_data) >= 3