from abc import ABC, abstractmethod

# support different alerting flavors: use an abstract class
class NotifyChannel(ABC):

    @abstractmethod
    async def notify(self, message):
        """ concrete send alert to this channel """
        pass