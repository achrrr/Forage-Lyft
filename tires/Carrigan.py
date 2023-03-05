from typing import List
from tire import Tire

class Carrigan(Tire):

    def __init__(self, tire_data:List[int]) -> None:     
        self.tire_data = tire_data
    
    def needs_service(self) -> bool:

        a:bool = False

        for n in self.tire_data:
            if n >= 0.9:
                a = True
        return a

        