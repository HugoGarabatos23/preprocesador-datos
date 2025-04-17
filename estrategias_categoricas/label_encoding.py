from estrategias_categoricas.estrategia_base import EstrategiaTransformacion
import pandas as pd

class LabelEncoding(EstrategiaTransformacion):
    def transformar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        df = df.copy()
        for col in columnas:
            df[col] = df[col].astype("category").cat.codes #convierte la columna en tipo "categoría" y le asigna un número interno a cada valor distinto.
        return df
