from notify import NotifyChannel

import requests

class NotifySlackWebhookl(NotifyChannel):
    def __init__(self, url):
        self.headers = {"content-type": "application/json"}
        self.url = url

    async def notify(self, message):
        payload = {
            "attachments": [
                {
                    "color": "#f00",
                    "text": message,
                }
            ]
        }
        response = requests.post(self.url, json=payload, headers=self.headers)

        if response.status_code != 200:
            logger("Cannot reach Slack API", log_type=log_types.WARNING)

