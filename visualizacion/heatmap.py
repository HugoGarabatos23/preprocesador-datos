import seaborn as sns
import matplotlib.pyplot as plt
from estado import AppState


class Heatmap:
    def crear_visualizacion(self, datos):
        """
        Crea un heatmap basado en la correlación entre las columnas numéricas de los datos.
        """
        estado = AppState()
        try:
            # Seleccionar solo columnas numéricas
            datos_numericos = datos.select_dtypes(include=['float64', 'int64'])

            # Calcular la matriz de correlación
            correlacion = datos_numericos.corr()

            # Crear el heatmap
            plt.figure(figsize=(10, 8))
            sns.heatmap(correlacion, annot=True, cmap='coolwarm',
                        fmt='.2f', linewidths=0.5)

            # Mostrar el heatmap
            plt.title("Heatmap de Correlación")
            plt.show()

            estado.heatmap = True
            print("✅ Heatmap generado exitosamente.")

        except Exception as e:
            print(f"❌ Error al crear el heatmap: {e}")
