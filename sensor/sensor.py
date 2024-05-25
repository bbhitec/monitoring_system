import random
from abc import ABC, abstractmethod


# support different sensor flavors: use an abstract class
# as per Dependency Inversion Principle SOLID principle
class Sensor(ABC):
    def __init__(self, sensor_type: str, valid_range: [float]):
        self.sensor_type = sensor_type
        self.valid_range = valid_range

    @abstractmethod
    async def read_value(self) -> float:
        """ simulate the sensor read-out """
        pass