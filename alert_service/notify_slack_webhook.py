from logger import logger, log_types

import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# load the environment to yse tokens
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


class NotifySlackWebhookl:
    def notify(self, message):
        url = os.environ['SLACK_WEBHOOK_URL']
        headers = {"content-type": "application/json"}
        payload = {
                "attachments": [
                    {
                        "fallback": "Plain-text summary of the attachment.",
                        "color": "#f00",
                        "text": message,
                    }
                ]
            }
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            logger("Cannot reach Slack API", log_type=log_types.WARNING)

