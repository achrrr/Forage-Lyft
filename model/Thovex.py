from datetime import datetime

from engine import CapuletEngine
from battery import NubbinBattery


class Thovex(CapuletEngine, NubbinBattery):
    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_needs_service():
            return True
        else:
            return False
