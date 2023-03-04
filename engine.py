
from abc import ABC, abstractmethod


class Engine(ABC):

    def __init__(self, current_milage:int, last_service_milage:int, warning_light_on:bool=False) -> None:
        
        self.current_milage = current_milage
        self.last_service_milage = last_service_milage
        self.warning_light_on = warning_light_on

    @abstractmethod
    def engine_needs_service():
        pass


class CapuletEngine(Engine):

    def __init__(self, current_milage:int, last_service_milage: int, warning_light_on: bool = False) -> None:
        super().__init__(current_milage, last_service_milage, 0)

        self.current_milage = current_milage
        self.last_service_milage = last_service_milage

    def engine_needs_service(self) -> bool:

        return self.current_milage - self.last_service_milage > 30000


class WilloughbyEngine(Engine):

    def __init__(self, current_milage: int, last_service_milage: int, warning_light_on: bool = False) -> None:
        super().__init__(current_milage, last_service_milage)

        self.current_milage = current_milage
        self.last_service_milage = last_service_milage
    
    def engine_needs_service(self) -> bool:
        return self.current_milage - self.last_service_milage > 60000

class SternmanEngine(Engine):

    def __init__(self, current_milage: int, last_service_milage: int, warning_light_on: bool = False) -> None:
        super().__init__(0,0, warning_light_on)

        self.warning_light_on = warning_light_on
    
    def engine_needs_service(self) -> bool:
        return self.warning_light_on



        
