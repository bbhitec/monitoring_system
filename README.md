# Sensor Data Monitoring and Alerting System

A python-based service to monitor sensor data
- Main service
    - Reads the provided config file
    - Initializes corresponding sensors and valid ranges
    - Continuously reads and validates data
    - Notifies the Aler service upon invalid range
- Alerts service
    - Receive alerts from the main server
    - Log the alert on desired channels

    ![System Class Diagram](https://raw.githubusercontent.com/bbhitec/monitoring_system/main/mon_class.png)

## Features
- Adhering SOLID principles
- Factory design pattern for the sensors types to separate creation from use
- Basic event-loop asynchronous sensor data polling
- Using flask server for REST communication between the sensors


## WIP
- [ ] Alert service flavors/channels: Email
- [ ] Unit testing

### Badges
![](https://shields.io/badge/-python-ffe600?logo=python)
![](https://shields.io/badge/-async-4377cb?logo=async)
![](https://shields.io/badge/-SOLID-4377cb)



## Possible upgrades to the system

- Sensors
    - Using a diagnostics poll layer to test integrity of sensor data (Hardware\Firmware level)
    - Provide a more robust logger service to output the readouts to interface with UI's and APi's
- Security/Reliability
    - Provide a layer to secure the sensors communication
    - A saved-stated soft\hard reset mechanism for emergency system refresh in cases of emergency failure/outage
    - Proper error/exception handling protocol
- Configuration
    - A dynamic configurations changes handling agent for a possible hot-swap of sensors
    - A defined or standard-compliant documentation on developer, technician, end user levels
- Performance/Scalability
    - The current async implememtation is a basic event-loop mechanism (if a certain sensor delays the read-out' for example, it will block the event loop). It can be prevented with some time-out feature or can further be upgraded to a subscriber model or a multi-threaded mechanism
    - Consider a mechanism (or 3rd party) metrics monitoring for reading latencies and response times
    - Consider cloud compute to handle large number of sensors with volume\performance pros and cons considerations and decoupling data collection and processing (e. g. using a message broker)
- Alerts
    - Using a server with per-customer defined channels (The given Mail and Slack alerts, also: Mobile client push notification, SMS, WhatsApp via Meta Suite or Twilio etc.)
A statistical/behavioral dashboard to diagnose and check alerts patterns, facilitate maintenance or replacement schedules



## Usage/How to run

_Pull the model:_</br>
```
git clone https://github.com/bbhitec/monitoring_system.git
```

_Virtual env recommended, Initialize:_</br>
```
py -3 -m venv .venv
```

_Activate:_</br>
```
.venv\scripts\activate
```

_Install additional dependencies:_</br>
```python
pip install -r requirements.txt
```

_Update the necessary environments in ```.env``` locally_</br>
_Use ```.env.template``` to see the used tokens_</br>
```
echo SLACK_WEBHOOK_URL = '<your url>' >> .env
```

_Run the alerting service server:_</br>
```python
python alert_service/alert_server.py
```

_Run the main script:_</br>
```python
python main.py
```

##### [vnik]
