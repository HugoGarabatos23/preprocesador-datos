# estrategias_nulos/rellenar_moda.py
from estrategias_nulos.estrategia_base import EstrategiaNulos
import pandas as pd

class RellenarModa(EstrategiaNulos):
    def aplicar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        df = df.copy()
        for col in columnas:
            if not df[col].mode().empty:
                df[col] = df[col].fillna(df[col].mode().iloc[0])
        return df
