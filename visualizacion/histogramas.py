# preprocesador_datos/visualizacion/histogramas.py
from estado import AppState
import matplotlib.pyplot as plt


class Histograma:
    def crear_visualizacion(self, estado: AppState):
        datos = estado.datos

        # Usar solo las features numéricas y transformadas
        columnas_validas = [
            col for col in estado.features
            if datos[col].dtype in ['int64', 'float64']
        ]

        if not columnas_validas:
            print("❌ No hay columnas numéricas adecuadas para crear un histograma.")
            return

        for col in columnas_validas:
            plt.figure(figsize=(8, 6))
            datos[col].hist(bins=20, edgecolor='black')
            plt.title(f"Histograma de {col}")
            plt.xlabel(col)
            plt.ylabel("Frecuencia")
            plt.show()

        # Cambiar el estado de visualización (para el histograma)
        estado.histograma = True
        print("✅ Histograma generado exitosamente.")
