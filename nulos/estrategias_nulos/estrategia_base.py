# estrategias_nulos/estrategia_base.py
from abc import ABC, abstractmethod
import pandas as pd


class EstrategiaNulos(ABC):
    @abstractmethod
    def aplicar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        pass
