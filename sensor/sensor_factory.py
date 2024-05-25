from sensor import Sensor
# from .sensor_concretes import TemperatureSensor, HumiditySensor, PressureSensor
from logger import logger, log_types

from datetime import datetime
import asyncio
import random
# from sensor import Sensor

FP_RESOLUTION = 4       # floating point accuracy
BUS_DELAY = 1.5         # general io bus pseudo-delay

class TemperatureSensor(Sensor):
    def __init__(self, valid_range: [float]):
        super().__init__("TemperatureSensor", valid_range)

    async def read_value(self) -> float:
        await asyncio.sleep(BUS_DELAY)  # pseudo io delay
        return round(random.uniform(-50, 150), FP_RESOLUTION)

class HumiditySensor(Sensor):
    def __init__(self, valid_range: [float]):
        super().__init__("HumiditySensor", valid_range)

    async def read_value(self) -> float:
        await asyncio.sleep(2)
        return round(random.uniform(0, 100), FP_RESOLUTION)

class PressureSensor(Sensor):
    def __init__(self, valid_range: [float]):
        super().__init__("PressureSensor", valid_range)

    async def read_value(self) -> float:
        await asyncio.sleep(BUS_DELAY)
        return round(random.uniform(800, 1200), FP_RESOLUTION)

class ProximitySensor(Sensor):
    def __init__(self, valid_range: [float]):
        super().__init__("ProximitySensor", valid_range)

    async def read_value(self) -> float:
        await asyncio.sleep(BUS_DELAY)
        return round(random.uniform(0, 5), FP_RESOLUTION)


class SensorFactory:
    sensor_types = {
        "TemperatureSensor": TemperatureSensor,
        "HumiditySensor": HumiditySensor,
        "PressureSensor": PressureSensor,
        "ProximitySensor": ProximitySensor
    }

    @staticmethod
    def create_sensor(sensor_type: str, valid_range: [float]) -> Sensor:
        if sensor_type in SensorFactory.sensor_types:
            return SensorFactory.sensor_types[sensor_type](valid_range)
        logger (f"Unrecognized sensor type: {sensor_type}", log_type=log_types.WARNING) # report illegal sensor type