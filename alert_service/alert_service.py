from datetime import datetime

import requests
import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv


class AlertService:
    def __init__(self):
        print("Alert service initiated")

    async def send_alert(self, message):
        dt = datetime.now()
        text = (f'ALERT [{dt}] {message}')
        print(f"\033[0;31m{text}\033[0m") # using ANSI color for alerts