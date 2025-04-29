import matplotlib.pyplot as plt
from estado import AppState
import pandas as pd


class DispersionPlot:
    def crear_visualizacion(self, estado: AppState):
        """
        Crea gráficos de dispersión comparando variables antes y después de la normalización.
        """
        try:
            if estado.datos_sin_normalizar is None:
                print("❌ No hay datos originales disponibles para comparar.")
                return

            datos_sin_normalizacion = estado.datos_sin_normalizar
            datos_norm = estado.datos
            features = estado.features

            for feature in features:
                if feature not in datos_sin_normalizacion.columns or feature not in datos_norm.columns:
                    continue
                if not pd.api.types.is_numeric_dtype(datos_sin_normalizacion[feature]):
                    continue

                plt.figure(figsize=(10, 5))

                # Gráfico lado a lado
                plt.subplot(1, 2, 1)
                plt.scatter(range(len(datos_sin_normalizacion)),
                            datos_sin_normalizacion[feature], alpha=0.5)
                plt.title(f"{feature} (Original)")
                plt.grid(True)

                plt.subplot(1, 2, 2)
                plt.scatter(range(len(datos_norm)),
                            datos_norm[feature], alpha=0.5, color='orange')
                plt.title(f"{feature} (Normalizado)")
                plt.grid(True)

                plt.suptitle(
                    f"Comparativa de '{feature}' antes y después de la normalización")
                plt.tight_layout()
                plt.show()

            estado.dispersion = True
            print("✅ Gráficos de dispersión comparativos generados correctamente.\n")

        except Exception as e:
            print(f"❌ Error al generar los gráficos de dispersión: {e}")
