# exportacion/estrategias_exportacion/exportador_base.py
from abc import ABC, abstractmethod
import pandas as pd


class Exportador(ABC):
    @property
    @abstractmethod
    def extension(self) -> str:
        """Extensión del archivo, como 'csv' o 'xlsx' """
        pass

    @abstractmethod
    def exportar(self, df: pd.DataFrame, nombre_archivo: str):
        pass
