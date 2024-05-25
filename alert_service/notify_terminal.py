class NotifyTerminal:
    """
    send alert to thr local terminal
    """
    def notify(self, message):
        print(f"\033[0;31m{message}\033[0m") # using ANSI color for attention-grabbing alerts