# preprocesador_datos/visualizacion/resumen_estadistico.py

import pandas as pd
from estado import AppState


class ResumenEstadistico:
    def crear_visualizacion(self, datos):
        estado = AppState()
        print("\n📊 Resumen Estadístico de los Datos")
        print("------------------------------------")
        # Incluye numéricas y categóricas
        resumen = datos.describe(include="all")
        print(resumen)
        estado.resumen_estadistico = True
