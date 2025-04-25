# estrategias_categoricas/estrategia_base.py
from abc import ABC, abstractmethod
import pandas as pd

class EstrategiaTransformacion(ABC):
    @abstractmethod
    def transformar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        pass
