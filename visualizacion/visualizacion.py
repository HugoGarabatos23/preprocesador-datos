from .resumen_estadistico import ResumenEstadistico
from .histogramas import Histograma
from .dispersion import DispersionPlot
from .heatmap import Heatmap
from estado import AppState


class Visualizacion:
    def mostrar_submenu_visualizacion(self, estado: AppState):
        """
        Muestra un submenú interactivo para que el usuario seleccione distintos tipos 
        de visualización de datos en la aplicación.

        El menú ofrece opciones para:
          - Resumen estadístico
          - Histogramas
          - Gráficos de dispersión (antes y después del preprocesamiento)
          - Heatmap (mapa de calor)
          - Volver al menú principal

        Parámetros:
        -----------
        estado : AppState
            Objeto que contiene el estado actual de la aplicación, incluyendo 
            los datos y configuraciones necesarias para generar las visualizaciones.

        Flujo:
        -------
        - Se muestra un menú con las opciones disponibles.
        - Según la opción seleccionada, se crea y muestra la visualización correspondiente.
        - El menú se repite hasta que el usuario seleccione la opción para volver al menú principal.
         - En caso de opción inválida, muestra un mensaje de error y vuelve a mostrar el menú.
        """

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
                factory.crear_visualizacion(estado)
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
