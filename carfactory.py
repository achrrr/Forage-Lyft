from car import Car
from datetime import datetime
from battery import Battery
from engine import Engine
import engine as eg
import battery as bt
from tires import Carrigan as cr
from tires import Octoprime as op



class CarFactory:
    
    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_data: list[int])-> Car:
        engine = eg.CapuletEngine(current_mileage, last_service_mileage)
        battery = bt.SpindlerBattery(current_date, last_service_date)
        tires = cr.Carrigan(tire_data)
        
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_data)-> Car:
        
        engine = eg.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = bt.SpindlerBattery(current_date, last_service_date)
        tires = op.Octoprime(tire_data)
        
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool, tire_data)-> Car:

        engine = eg.SternmanEngine(warning_light_on)
        battery = bt.SpindlerBattery(current_date, last_service_date)
        tires = cr.Carrigan(tire_data)
        
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_data)-> Car:
        
        engine = eg.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = bt.NubbinBattery(current_date, last_service_date)
        tires = op.Octoprime(tire_data)
        
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_data) -> Car:
        
        engine = eg.CapuletEngine(current_mileage, last_service_mileage)
        battery = bt.NubbinBattery(current_date, last_service_date)
        tires = op.Octoprime(tire_data)
        
        return Car(engine, battery, tires)