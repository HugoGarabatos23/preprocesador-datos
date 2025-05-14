from outliers.tratamiento_outliers.outliers_interface import OutlierHandler


class ReplaceOutliersWithMedian(OutlierHandler):
    def handle_outliers(self):
        for col, idxs in self.outliers_info.items():
            # Crear una serie sin los outliers
            non_outliers = self.df[~self.df.index.isin(idxs)][col]
            median = non_outliers.median()
            # Reemplazar outliers por la mediana calculada
            self.df.loc[idxs, col] = median
        print("Valores atípicos reemplazados con la mediana (calculada sin outliers) de cada columna.")
