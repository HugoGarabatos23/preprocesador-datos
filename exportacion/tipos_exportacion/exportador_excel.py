# exportacion/estrategias_exportacion/exportador_excel.py
import pandas as pd
from exportacion.exportador_base import Exportador
from estado import AppState


class ExportadorExcel(Exportador):
    @property
    def extension(self) -> str:
        return "xlsx"

    def exportar(self, df: pd.DataFrame, nombre_archivo: str):
        estado = AppState()
        df.to_excel(f"{nombre_archivo}.xlsx", index=False)
        print(
            f"✅ Datos exportados correctamente como \"{nombre_archivo}.xlsx\".")
        estado.formato_xlsx = True
