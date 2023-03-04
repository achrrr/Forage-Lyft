from abc import ABC, abstractmethod
from datetime import datetime
from battery import Battery
from engine import Engine
import engine as eg
import battery as bt


class Serviceable(ABC):

    @abstractmethod
    def needs_service() -> bool:
        pass

class Car(Serviceable):
    
    def __init__(self, engine: Engine, battery: Battery) -> None:
        super().__init__()

        self.engine = engine
        self.battery = battery
    def needs_service(self) -> bool:
        return self.engine.engine_needs_service() or self.battery.battery_needs_service()

class CarFactory(Engine):

    def __init__(self, engine: Engine, battery: Battery) -> Car:
        pass

    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int)-> Car:
        engine = eg.CapuletEngine(current_milage=current_mileage, last_service_milage=last_service_mileage)
        battery = bt.SpindlerBattery(last_service_date=last_service_date)
        
        return Car(engine, battery)
    
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int)-> Car:
        
        engine = eg.WilloughbyEngine(current_milage=current_mileage, last_service_milage=last_service_mileage)
        battery = bt.SpindlerBattery(last_service_date=last_service_date)
        
        return Car(engine, battery)
    
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool)-> Car:

        engine = eg.SternmanEngine()
        battery = bt.SpindlerBattery(last_service_date=last_service_date)
        
        return Car(engine, battery)
    
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int)-> Car:
        
        engine = eg.WilloughbyEngine(current_milage=current_mileage, last_service_milage=last_service_mileage)
        battery = bt.NubbinBattery(last_service_date=last_service_date)
        
        return Car(engine, battery)

    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        
        engine = eg.CapuletEngine(current_milage=current_mileage, last_service_milage=last_service_mileage)
        battery = bt.NubbinBattery(last_service_date=last_service_date)
        
        return Car(engine, battery)

    
