from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def engine_needs_service(self)-> bool:
        pass

class CapuletEngine(Engine):

    def __init__(self, current_milage:int, last_service_milage: int) -> None:

        self.current_milage = current_milage
        self.last_service_milage = last_service_milage

    def engine_needs_service(self) -> bool:

        return self.current_milage - self.last_service_milage > 30000


class WilloughbyEngine(Engine):

    def __init__(self, current_milage: int, last_service_milage: int) -> None:

        self.current_milage = current_milage
        self.last_service_milage = last_service_milage
    
    def engine_needs_service(self) -> bool:
        return self.current_milage - self.last_service_milage > 60000

class SternmanEngine(Engine):

    def __init__(self, warning_light_on: bool = False) -> None:

        self.warning_light_on = warning_light_on
    
    def engine_needs_service(self) -> bool:
        return self.warning_light_on



        
