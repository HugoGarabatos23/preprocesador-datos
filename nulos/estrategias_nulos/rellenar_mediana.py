# estrategias_nulos/rellenar_mediana.py
from estrategias_nulos.estrategia_base import EstrategiaNulos
import pandas as pd

class RellenarMediana(EstrategiaNulos):
    def aplicar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        df = df.copy()
        for col in columnas:
            if df[col].dtype.kind in 'biufc':
                df[col] = df[col].fillna(df[col].median())
        return df
