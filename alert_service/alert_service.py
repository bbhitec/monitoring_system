from notify_terminal import NotifyTerminal
from notify_slack_webhook import NotifySlackWebhookl

from datetime import datetime
import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv


class AlertService:
    def __init__(self):

        # currently the alerting channels are hardcoded
        # and implementation specific
        notifier_terminal = NotifyTerminal()

        # setting up the slack alerting service
        # load the environment variables to use tokens
        env_path = Path('.')/'.env'
        load_dotenv(dotenv_path=env_path)
        try:
            url = os.environ['SLACK_WEBHOOK_URL']
            notifier_slack = NotifySlackWebhookl(url)
        except KeyError:
            print("SlackWebHook API not found")
            notifier_slack = None

        notifier_sms = None
        notifier_email = None

        self.alert_channels = [
            notifier_terminal,
            notifier_slack,
            notifier_sms,
            notifier_email]

        print("Alert service initiated")


    async def send_alert(self, message):
        """ prepare alert text and send alert to all defined channels """

        # format alert text
        dt = datetime.now()
        text = (f'ALERT!! [{dt}] {message}')

        # asynchronously alert all the valid channels
        tasks = []
        for channel in self.alert_channels:
            if channel:
                tasks.append(asyncio.create_task(channel.notify(text)))
        await asyncio.gather(*tasks)