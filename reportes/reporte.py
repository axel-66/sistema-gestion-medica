from abc import ABC, abstractmethod
from datetime import date


class Reporte(ABC):

    def __init__(self):
        self.__fechaGeneracion = date.today()

    @abstractmethod
    def generar(self):
        pass

    @property
    def fechaGeneracion(self):
        return self.__fechaGeneracion