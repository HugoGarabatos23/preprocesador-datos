# estrategias_nulos/rellenar_media.py
from estrategias_nulos.estrategia_base import EstrategiaNulos
import pandas as pd

class RellenarMedia(EstrategiaNulos):
    def aplicar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        df = df.copy()
        for col in columnas:
            if df[col].dtype.kind in 'biufc':  # numérico
                df[col] = df[col].fillna(df[col].mean())
        return df
 