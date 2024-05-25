from sensor import Sensor
import asyncio
import random

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
