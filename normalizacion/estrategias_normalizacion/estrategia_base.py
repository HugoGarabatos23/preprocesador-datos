# estrategias_normalizacion/estrategia_base.py
from abc import ABC, abstractmethod
import pandas as pd


class EstrategiaNormalizacion(ABC):
    @abstractmethod
    def aplicar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        pass
