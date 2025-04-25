# estrategias_nulos/eliminar_filas.py
from estrategias_nulos.estrategia_base import EstrategiaNulos
import pandas as pd

class EliminarFilas(EstrategiaNulos):
    def aplicar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        return df.dropna(subset=columnas)
