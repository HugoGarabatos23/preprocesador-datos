import pandas as pd
from abc import ABC, abstractmethod


class OutlierHandler(ABC):
    def __init__(self, df: pd.DataFrame, numeric_columns: list):
        self.df = df.copy()
        self.numeric_columns = numeric_columns
        self.outliers_info = {}

    def execute(self):
        self.detect_outliers()
        if not self.outliers_info:
            print("No se han detectado valores atípicos en las columnas seleccionadas.")
            return self.df, False

        self.show_outliers_report()
        self.handle_outliers()
        return self.df, True

    def detect_outliers(self):
        for col in self.numeric_columns:
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            mask = (self.df[col] < lower_bound) | (self.df[col] > upper_bound)
            outliers = self.df[mask]
            if not outliers.empty:
                self.outliers_info[col] = outliers.index.tolist()

    def show_outliers_report(self):
        print("Se han detectado valores atípicos en las siguientes columnas:")
        for col, idxs in self.outliers_info.items():
            print(f"  - {col}: {len(idxs)} valores atípicos detectados")

    @abstractmethod
    def handle_outliers(self):
        pass
