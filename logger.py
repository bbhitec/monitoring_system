from datetime import datetime
from enum import Enum

class log_types(Enum):
    DEFAULT = 0
    READING = 1
    WARNING = 2

log_headers = {
    log_types.DEFAULT:    "LOGGING",
    log_types.READING:    "READING",
    log_types.WARNING:    "WARNING",
}

def logger(message, log_type = log_types.DEFAULT):
    """separated local logger functionality"""
    dt = datetime.now()
    print(f"{log_headers[log_type]} [{dt}] {message}")