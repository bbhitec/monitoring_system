from notify import NotifyChannel

class NotifyTerminal(NotifyChannel):
    """
    send alert to thr local terminal
    """
    async def notify(self, message):
        print(f"\033[0;31m{message}\033[0m") # using ANSI color for attention-grabbing alerts