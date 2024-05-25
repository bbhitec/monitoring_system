from monitoring_service import SensorMonitoringService
from constants import ALERT_SERVER_URL

import asyncio


if __name__ == "__main__":
    # the alerting server will be communicated via the url
    alert_services_url = ALERT_SERVER_URL
    monitoring_service = SensorMonitoringService('config.json', alert_services_url=alert_services_url)

    try:
        asyncio.run(monitoring_service.start_service())
    except KeyboardInterrupt:
        print("Ctrl+C detected, exiting...")
    except Exception as e:
        print(f'Failed with: {e}')

