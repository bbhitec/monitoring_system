import random
from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, sensor_type: str, valid_range: [float]):
        self.sensor_type = sensor_type
        self.valid_range = valid_range

    @abstractmethod
    async def read_value(self) -> float:
        """simulate a sensor read-out"""
        pass