# exportacion/estrategias_exportacion/exportador_csv.py
import pandas as pd
from exportacion.exportador_base import Exportador
from estado import AppState


class ExportadorCSV(Exportador):
    @property
    def extension(self) -> str:
        return "csv"

    def exportar(self, df: pd.DataFrame, nombre_archivo: str):
        estado = AppState()
        df.to_csv(f"{nombre_archivo}.csv", index=False)
        print(
            f"✅ Datos exportados correctamente como \"{nombre_archivo}.csv\".")
        estado.formato_csv = True
