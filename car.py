from abc import ABC, abstractmethod
from datetime import datetime
from battery import Battery
from engine import Engine
from tire import Tire

class Serviceable(ABC):

    @abstractmethod
    def needs_service() -> bool:
        pass
class Car(Serviceable):
    
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):

        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool:
        return self.engine.engine_needs_service() or self.battery.battery_needs_service() or self.tire.needs_service()
    
