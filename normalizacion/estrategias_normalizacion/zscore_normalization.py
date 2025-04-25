from normalizacion.estrategias_normalizacion.estrategia_base import EstrategiaNormalizacion
import pandas as pd


class ZScoreNormalization(EstrategiaNormalizacion):
    def aplicar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        df = df.copy()
        for col in columnas:
            media = df[col].mean()
            std = df[col].std()
            df[col] = (df[col] - media) / std
        return df
