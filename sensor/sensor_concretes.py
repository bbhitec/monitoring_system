from sensor import Sensor
import asyncio
import random

N = 4
BUS_DELAY = 5

class TemperatureSensor(Sensor):
    def __init__(self, valid_range: [float]):
        super().__init__("TemperatureSensor", valid_range)

    async def read_value(self) -> float:
        await asyncio.sleep(BUS_DELAY)  # Simulate I/O delay
        return round(random.uniform(-50, 150), N)

class HumiditySensor(Sensor):
    def __init__(self, valid_range: [float]):
        super().__init__("HumiditySensor", valid_range)

    async def read_value(self) -> float:
        await asyncio.sleep(0.1)  # Simulate I/O delay
        return round(random.uniform(0, 100), N)

class PressureSensor(Sensor):
    def __init__(self, valid_range: [float]):
        super().__init__("PressureSensor", valid_range)

    async def read_value(self) -> float:
        await asyncio.sleep(BUS_DELAY)  # Simulate I/O delay
        return round(random.uniform(800, 1200), N)
