from abc import ABC, abstractmethod
from datetime import datetime

class Battery(ABC):
    @abstractmethod
    def battery_needs_service(self):
        pass

class SpindlerBattery(Battery):

    def __init__(self, current_date, last_service_date:datetime) -> None:

        self.current_date = current_date
        self.last_service_date = last_service_date

    def battery_needs_service(self) -> bool:
        
        threshold_date:datetime = self.last_service_date.replace(year = self.last_service_date.year + 3)

        if threshold_date < self.current_date:
            return True
        else:
            return False

class NubbinBattery(Battery):

    def __init__(self, current_date, last_service_date: datetime):
        
        self.current_date = current_date
        self.last_service_date = last_service_date

    def battery_needs_service(self) -> bool:
        threshold_date:datetime =  self.last_service_date.replace(year = self.last_service_date.year + 4)

        if threshold_date < self.current_date:
            return True
        else:
            return False

