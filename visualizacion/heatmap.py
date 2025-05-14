import seaborn as sns
import matplotlib.pyplot as plt
from estado import AppState


class Heatmap:
    def crear_visualizacion(self, estado: AppState):
        """
        Crea un heatmap basado en la correlación entre las columnas numéricas de los datos.
        """
        datos = estado.datos
        try:
            # Seleccionar solo columnas numéricas
            datos_numericos = datos.select_dtypes(include=['float64', 'int64'])

            if datos_numericos.shape[1] < 2:
                print(
                    "❌ No hay columnas numéricas adecuadas para crear un mapa de calor.")
                return

            # Calcular la matriz de correlación
            correlacion = datos_numericos.corr()

            if correlacion.empty or correlacion.shape[0] < 2:
                print("❌ No hay suficientes datos para crear un mapa de calor.")
                return

            # Crear el heatmap
            plt.figure(figsize=(10, 8))
            sns.heatmap(correlacion, annot=True, cmap='coolwarm',
                        fmt='.2f', linewidths=0.5)

            # Mostrar el heatmap
            plt.title("Heatmap de Correlación")
            plt.show()

            estado.heatmap = True
            print("✅ Mapa de calor generado exitosamente.")

        except Exception as e:
            print(f"❌ Error al crear el heatmap: {e}")
