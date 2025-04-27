# preprocesador_datos/visualizacion/histogramas.py
from estado import AppState
import matplotlib.pyplot as plt


class Histograma:
    def crear_visualizacion(self, estado: AppState):
        datos = estado.datos

        columnas_numericas = [
            col for col in datos.columns if datos[col].dtype in ['int64', 'float64']]

        if not columnas_numericas:
            print("❌ No hay columnas numéricas para crear un histograma.")
            return

        for col in columnas_numericas:
            plt.figure(figsize=(8, 6))
            datos[col].hist(bins=20, edgecolor='black')
            plt.title(f"Histograma de {col}")
            plt.xlabel(col)
            plt.ylabel("Frecuencia")
            plt.show()

        # Cambiar el estado de visualización (para el histograma)
        estado.histograma = True
        print("✅ Histograma generado exitosamente.")
