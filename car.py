from abc import ABC, abstractmethod
from datetime import datetime
from battery import Battery
from dataclasses import dataclass
from engine import Engine
import engine as eg
import battery as bt


class Serviceable(ABC):

    @abstractmethod
    def needs_service() -> bool:
        pass


class Car(Serviceable):
    
    def __init__(self, engine:Engine, battery: Battery) -> None:
        super().__init__()

    def needs_service() -> bool:
        return Engine.engine_needs_service() or Battery.battery_needs_service()

class CarFactory(Engine):

    def __init__(self, engine: Engine, battery: Battery) -> Car:
        pass

    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int)-> Car:

        return Car(eg.CapuletEngine, bt.SpindlerBattery)
    
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int)-> Car:
        return Car(eg.WilloughbyEngine, bt.SpindlerBattery)
    
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool)-> Car:
        return Car(eg.SternmanEngine, bt.SpindlerBattery)
    
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int)-> Car:
        return Car(eg.WilloughbyEngine, bt.NubbinBattery)

    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(eg.CapuletEngine, bt.NubbinBattery)

o = CarFactory.create_calliope(12, 1, 1, 1)


    