from sensor import Sensor
from alert_service import AlertService
from logger import logger, log_types

import asyncio
from typing import List
from datetime import datetime

READ_FREQUENCY = 0  # monitor every READ_FREQUENCY seconds


class SensorMonitor:
    """ de-coupling the monitoring functionality spescifics """
    def __init__(self, sensor: Sensor, alert_service):
        self.sensor = sensor
        self.alert_service = alert_service

    async def validate_sensor_data(self):
        # read sensor data and test it
        value = await self.sensor.read_value()

        if not(self.sensor.valid_range[0] <= value <= self.sensor.valid_range[1]):
            # the alerting service will use any define notification channels (terminal, Slack...)
            await self.alert_service.send_alert(
                f"Invalid data - {self.sensor.sensor_type}: {value} range[{self.sensor.valid_range[0]},{self.sensor.valid_range[1]}]")
        else:
            logger(f"Value read from {self.sensor.sensor_type}: {value}", log_type=log_types.READING)

    async def start_monitoring(self):
        while True:
            await self.validate_sensor_data()
            await asyncio.sleep(READ_FREQUENCY)  # wait the interval between readings