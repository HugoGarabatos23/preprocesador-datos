from outliers.tratamiento_outliers.outliers_interface import OutlierHandler


class ReplaceOutliersWithMedian(OutlierHandler):
    def handle_outliers(self):
        for col, idxs in self.outliers_info.items():
            median = self.df[col].median()
            self.df.loc[idxs, col] = median
        print("Valores atípicos reemplazados con la mediana de cada columna.")
