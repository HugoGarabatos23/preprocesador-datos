# estrategias_nulos/rellenar_constante.py
from nulos.estrategias_nulos.estrategia_base import EstrategiaNulos
import pandas as pd


class RellenarConstante(EstrategiaNulos):
    def __init__(self, valor_constante):
        self.valor = valor_constante

    def aplicar(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        df = df.copy()
        for col in columnas:
            df[col] = df[col].fillna(self.valor)
        return df
