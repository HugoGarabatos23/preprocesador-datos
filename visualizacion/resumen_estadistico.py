from estado import AppState
import pandas as pd


class ResumenEstadistico:
    def crear_visualizacion(self, estado: AppState):
        datos = estado.datos[estado.features + [estado.target]]

        print("\n📊 Resumen Estadístico de los Datos")
        print("-" * 60)

        # Separar columnas numéricas y categóricas
        columnas_numericas = datos.select_dtypes(include=["number"]).columns
        columnas_categoricas = datos.select_dtypes(
            include=["object", "category", "bool"]).columns

        # Filtrar columnas numéricas válidas (descartando codificadas y binarias)
        columnas_numericas_validas = [
            col for col in columnas_numericas
            if col not in estado.columnas_codificadas and col not in estado.columnas_binarias
        ]

        # Estadísticas para numéricas
        if columnas_numericas_validas:
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

            if estado.columnas_codificadas or estado.columnas_binarias:
                print(
                    "\n Se han excluido del resumen estadístico las siguientes columnas transformadas desde variables categóricas:")
                if estado.columnas_codificadas:
                    print(
                        f" Codificadas con Label Encoding: {estado.columnas_codificadas}\n")
                if estado.columnas_binarias:
                    print(
                        f" Generadas con One-Hot Encoding (columnas binarias): {estado.columnas_binarias}\n")

            print(resumen_numerico.round(2))

        # Distribuciones categóricas
        if len(columnas_categoricas) > 0:
            print("\n Variables Categóricas:")
            for col in columnas_categoricas:
                print(f"\n Distribución de '{col}':")
                print(datos[col].value_counts())

        estado.resumen_estadistico = True
