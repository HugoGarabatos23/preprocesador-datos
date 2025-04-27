# preprocesador_datos/visualizacion/factory_visualizacion.py

from .resumen_estadistico import ResumenEstadistico
from .histogramas import Histograma
from .dispersion import DispersionPlot
from .heatmap import Heatmap
from estado import AppState


class Visualizacion:
    def mostrar_submenu_visualizacion(self, estado: AppState):
        visualizacion = True
        while visualizacion:
            print("\n=============================")
            print("Visualización de Datos")
            print("=============================")
            print("  [1] Resumen estadístico")
            print("  [2] Histogramas")
            print("  [3] Dispersión antes/después")
            print("  [4] Heatmap")
            print("  [5] Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                factory = ResumenEstadistico()
                print(factory.crear_visualizacion(estado))
            elif opcion == "2":
                factory = Histograma()
                factory.crear_visualizacion(estado)
            elif opcion == "3":
                factory = DispersionPlot()
                factory.crear_visualizacion(estado)
            elif opcion == "4":
                factory = Heatmap()
                factory.crear_visualizacion(estado)
            elif opcion == "5":
                visualizacion = False
            else:
                print("Opción no válida. Intente de nuevo.")
