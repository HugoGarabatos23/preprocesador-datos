from estado import AppState


class ResumenEstadistico:
    def crear_visualizacion(self, estado: AppState):
        datos = estado.datos
        print("\n📊 Resumen Estadístico de los Datos")
        print("------------------------------------")
        # Incluye numéricas y categóricas
        resumen = datos.describe(include="all")
        print(resumen)
        estado.resumen_estadistico = True
