from categoricos.estrategias_categoricas.estrategia_base import EstrategiaTransformacion
import pandas as pd


class OneHotEncoding(EstrategiaTransformacion):
    def transformar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        # sintaxis de pandas
        return pd.get_dummies(df, columns=columnas, drop_first=False)
