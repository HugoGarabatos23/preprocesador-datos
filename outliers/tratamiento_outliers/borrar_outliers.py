from outliers.tratamiento_outliers.outliers_interface import OutlierHandler


class RemoveOutliers(OutlierHandler):
    def handle_outliers(self):
        indices_to_remove = set(
            i for idxs in self.outliers_info.values() for i in idxs)
        self.df.drop(index=indices_to_remove, inplace=True)
        print("Filas con valores atípicos eliminadas.")
