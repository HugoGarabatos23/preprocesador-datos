import pandas as pd
import matplotlib.pyplot as plt
from estado import AppState


class DispersionPlot:
    def crear_visualizacion(self, estado: AppState):
        """
        Crea gráficos de dispersión entre las features seleccionadas y el target.
        """
        try:
            datos = estado.datos
            features = estado.features
            target = estado.target
            for feature in features:
                if pd.api.types.is_numeric_dtype(datos[feature]):
                    plt.figure(figsize=(8, 6))
                    plt.scatter(datos[feature], datos[target], alpha=0.5)
                    plt.title(f"Dispersión: {feature} vs {target}")
                    plt.xlabel(feature)
                    plt.ylabel(target)
                    plt.grid(True)
                    plt.show()

            # Cambiar el estado
            estado.dispersion = True

            print("✅ Gráficos de dispersión generados correctamente.\n")

        except Exception as e:
            print(f"❌ Error al generar los gráficos de dispersión: {e}")
