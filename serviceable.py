from abc import ABC, abstractmethod

# this is an interface

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass