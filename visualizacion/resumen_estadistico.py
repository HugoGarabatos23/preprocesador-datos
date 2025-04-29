from estado import AppState
import pandas as pd


class ResumenEstadistico:
    def crear_visualizacion(self, estado: AppState):
        datos = estado.datos

        print("\n📊 Resumen Estadístico de los Datos")
        print("-" * 60)

        # Separar columnas numéricas y categóricas
        columnas_numericas = datos.select_dtypes(include=["number"]).columns
        columnas_categoricas = datos.select_dtypes(
            include=["object", "category", "bool"]).columns

        # Estadísticas para numéricas
        if not columnas_numericas.empty:
            print("\n📈 Variables Numéricas:")
            resumen_numerico = pd.DataFrame({
                "Media": datos[columnas_numericas].mean(),
                "Mediana": datos[columnas_numericas].median(),
                "Desviación Estándar": datos[columnas_numericas].std(),
                "Q1 (25%)": datos[columnas_numericas].quantile(0.25),
                "Q3 (75%)": datos[columnas_numericas].quantile(0.75),
                "Mínimo": datos[columnas_numericas].min(),
                "Máximo": datos[columnas_numericas].max(),
            })
            print(resumen_numerico.round(2))

        # Distribuciones categóricas
        if len(columnas_categoricas) > 0:
            print("\n Variables Categóricas:")
            for col in columnas_categoricas:
                print(f"\n Distribución de '{col}':")
                print(datos[col].value_counts())

        estado.resumen_estadistico = True
