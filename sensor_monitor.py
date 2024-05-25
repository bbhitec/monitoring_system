from sensor import Sensor
from logger import logger, log_types
from constants import ALERT_SERVER_URL, READ_FREQUENCY, STATUS_OK

import requests
import asyncio


class SensorMonitor:
    """ de-coupling the monitoring functionality spescifics """
    def __init__(self, sensor: Sensor, alert_services_url=ALERT_SERVER_URL):
        self.sensor = sensor
        self.alert_services_url = alert_services_url

    async def validate_sensor_data(self):
        # read sensor data and test it
        value = await self.sensor.read_value()

        if not(self.sensor.valid_range[0] <= value <= self.sensor.valid_range[1]):

            alert_message  = (f"Invalid data: {self.sensor.sensor_type}: {value} range[{self.sensor.valid_range[0]},{self.sensor.valid_range[1]}]")

            # the alerting service will use any defined notification channels (terminal, Slack...)
            # request via HTTP API communication
            payload = {"text": alert_message}

            response = requests.post(self.alert_services_url, json=payload)
            if response.status_code != 200:
                logger("Alert service request failed")
            else:
                logger(f"Alerted: {alert_message}")


        else:
            logger(f"Value read from {self.sensor.sensor_type}: {value}", log_type=log_types.READING)


    async def start_monitoring(self):
        while True:
            await self.validate_sensor_data()
            await asyncio.sleep(READ_FREQUENCY)  # wait the interval between readings