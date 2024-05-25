from sensor import SensorFactory
from sensor_monitor import SensorMonitor
from logger import logger, log_types
from constants import ALERT_SERVER_URL

import json
import asyncio
import requests


class SensorMonitoringService:
    def __init__(self, config_file, alert_services_url=ALERT_SERVER_URL):
        self.config_file = config_file
        self.alert_services_url = alert_services_url
        self.sensor_monitors = []
        self.sensors = []
        self.load_configuration()

    def load_configuration(self):
        with open(self.config_file, 'r') as f:
            config = json.load(f)

            # initialize/'connect' each configured sensor
            for sensor_config in config["sensors"]:
                sensor_type = sensor_config["type"]
                valid_range = sensor_config["valid_range"]
                sensor = SensorFactory.create_sensor(sensor_type, valid_range)

                # check if the sensor type is legal, skip unknown sensors
                if (sensor):
                    self.sensors.append(sensor)
                    sensor_monitor = SensorMonitor(sensor, self.alert_services_url)
                    self.sensor_monitors.append(sensor_monitor)
                else:
                    logger (f"Sensor not initialized: {sensor_type}", log_type=log_types.WARNING)

                # consider case: no valid sensors in config
                if (not self.sensors):
                    logger (f"No valid sensors to monitor. Terminating...", log_type=log_types.WARNING)
                    exit()

    async def start_service(self):
        try:
            tasks = [asyncio.create_task(sensor_monitor.start_monitoring()) for sensor_monitor in self.sensor_monitors]
            await asyncio.gather(*tasks)    # we can further use TaskPool here for a more elegant error handling
        except requests.ConnectionError:
            # handle server stop or disconnection
            logger(f"Alert server connection error. Exiting...")

