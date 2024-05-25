from alert_service import AlertService
from monitoring_service import SensorMonitoringService
import asyncio

if __name__ == "__main__":
    alert_service = AlertService()
    monitoring_service = SensorMonitoringService('config.json', alert_service)

    asyncio.run(monitoring_service.start_monitoring())
