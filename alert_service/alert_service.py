from .notify_terminal import NotifyTerminal
from .notify_slack_webhook import NotifySlackWebhookl

from datetime import datetime
from enum import Enum
import asyncio
import requests
import os


class alert_channels(Enum):
    TERMINAL = 0
    SLACK = 1
    MAIL = 2

class AlertService:
    def __init__(self):
        print("Alert service initiated")

    async def send_alert(self, message):
        """ prepare alert text and send alert to all defined channels """

        # format alert text
        dt = datetime.now()
        text = (f'ALERT!! [{dt}] {message}')

        # for now the alerting channels are hardcoded
        # # and implementation specific
        notifier_terminal = NotifyTerminal()
        notifier_slack = NotifySlackWebhookl()
        notifier_sms = None
        notifier_email = None

        alert_channels = [notifier_terminal, notifier_slack]
        for channel in alert_channels:
            if channel:
                channel.notify(text)