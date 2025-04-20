from outliers_interface import OutlierHandler


class KeepOutliers(OutlierHandler):
    def handle_outliers(self):
        print("Valores atípicos mantenidos sin cambios.")
