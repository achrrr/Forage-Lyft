from abc import ABC, abstractmethod
from datetime import datetime

class Battery(ABC):

    def __init__(self, last_service_date:datetime):

        self.last_service_date = last_service_date


    @abstractmethod
    def battery_needs_service(self):
        pass

class SpindlerBattery(Battery):

    def __init__(self, last_service_date:datetime) -> None:
        super().__init__(last_service_date)

        self.last_service_date = last_service_date

    def battery_needs_service(self):
        
        threshold_date:datetime = self.last_service_date.replace(year = self.last_service_date.year + 3)

        return True if threshold_date < datetime.today().date() else False


class NubbinBattery(Battery):

    def __init__(self, last_service_date: datetime):
        super().__init__(last_service_date)
        
        self.last_service_date = last_service_date

    def battery_needs_service(self):
        threshold_date:datetime =  self.last_service_date.replace(year = self.last_service_date.year + 4)

        return True if threshold_date < datetime.today().date() else False
