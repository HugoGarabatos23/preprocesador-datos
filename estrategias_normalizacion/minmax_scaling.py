from estrategias_normalizacion.estrategia_base import EstrategiaNormalizacion
import pandas as pd


class MinMaxScaling(EstrategiaNormalizacion):
    def aplicar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        df = df.copy()
        for col in columnas:
            min_val = df[col].min()
            max_val = df[col].max()
            df[col] = (df[col] - min_val) / (max_val - min_val)
        return df
