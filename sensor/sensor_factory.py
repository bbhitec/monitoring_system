from sensor import Sensor
from .sensor_concretes import TemperatureSensor, HumiditySensor, PressureSensor
from logger import logger, log_types


from datetime import datetime

class SensorFactory:
    sensor_types = {
        "TemperatureSensor": TemperatureSensor,
        "HumiditySensor": HumiditySensor,
        "PressureSensor": PressureSensor
    }

    @staticmethod
    def create_sensor(sensor_type: str, valid_range: [float]) -> Sensor:
        if sensor_type in SensorFactory.sensor_types:
            return SensorFactory.sensor_types[sensor_type](valid_range)
        logger (f"Unrecognized sensor type: {sensor_type}", log_type=log_types.WARNING) # report illegal sensor type