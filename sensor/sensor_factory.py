from sensor import Sensor
from .sensor_concretes import TemperatureSensor, HumiditySensor, PressureSensor

# from sensor_concretes import TemperatureSensor
# import sensor_concretes

class SensorFactory:
    # sensor_types: Dict[str, Type[Sensor]] = {
    sensor_types = {
        "TemperatureSensor": TemperatureSensor,
        "HumiditySensor": HumiditySensor,
        "PressureSensor": PressureSensor
    }

    # @staticmethod
    def create_sensor(sensor_type: str, valid_range: [float]) -> Sensor:
        if sensor_type in SensorFactory.sensor_types:
            return SensorFactory.sensor_types[sensor_type](valid_range)
        raise ValueError(f"Unknown sensor type: {sensor_type}")