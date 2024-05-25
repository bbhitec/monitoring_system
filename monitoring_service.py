# from sensor import TemperatureSensor, HumiditySensor, PressureSensor
from sensor import SensorFactory

from datetime import datetime
import json
import asyncio

READ_FREQUENCY = 2 # Monitor every READ_FREQUENCY seconds


class SensorMonitoringService:
    def __init__(self, config_file, alert_service):
        self.config_file = config_file
        self.alert_service = alert_service
        self.sensors = []
        self.load_configuration()

    def load_configuration(self):
        with open(self.config_file, 'r') as f:
            config = json.load(f)
            for sensor_config in config["sensors"]:
                # initialize/'connect' each configured sensor
                sensor_type = sensor_config["type"]
                valid_range = sensor_config["valid_range"]
                sensor = SensorFactory.create_sensor(sensor_type, valid_range)
                self.sensors.append(sensor)

                # [wip] consider case: no sensors in config

                # if sensor_type == "TemperatureSensor":
                #     self.sensors.append(TemperatureSensor(valid_range))
                # elif sensor_type == "HumiditySensor":
                #     self.sensors.append(HumiditySensor(valid_range))
                # elif sensor_type == "PressureSensor":
                #     self.sensors.append(PressureSensor(valid_range))

    async def validate_sensor_data(self, sensor):
        value = await sensor.read_value()
        if not(sensor.valid_range[0] <= value <= sensor.valid_range[1]):
            await self.alert_service.send_alert(f"Invalid data - {sensor.sensor_type}: {value} range[{sensor.valid_range[0]},{sensor.valid_range[1]}]")
        else:
            dt = datetime.now()
            print(f"READS [{dt}]: Value read from {sensor.sensor_type}: {value}")

    async def start_monitoring(self):
        while True:
            # [wip] consider asyncio.create_task() here
            tasks = [self.validate_sensor_data(sensor) for sensor in self.sensors]
            await asyncio.gather(*tasks)    # consider (TaskGroup) safer mechanism than gather

            # [wip] turn the sleep back on
            # await asyncio.sleep(READ_FREQUENCY)
