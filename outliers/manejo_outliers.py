from outliers.tratamiento_outliers.borrar_outliers import RemoveOutliers
from outliers.tratamiento_outliers.sustituir_outliers import ReplaceOutliersWithMedian
from outliers.tratamiento_outliers.mantener_outliers import KeepOutliers
import pandas as pd
from estado import AppState


def mostrar_submenu_manejo_outliers(estado: AppState):
    """
    Muestra el submenú para la detección y manejo de valores atípicos (outliers) en las columnas numéricas seleccionadas.

    Requiere que la normalización de datos haya sido completada previamente.
    Evalúa columnas numéricas con más de dos valores únicos para evitar columnas binarias.
    Realiza una detección preliminar de outliers y muestra un reporte si se encuentran.
    Permite al usuario elegir entre las siguientes estrategias:
      - Eliminar filas con valores atípicos
      - Reemplazar valores atípicos con la mediana de la columna
      - Mantener los valores atípicos sin cambios
      - Volver al menú principal sin aplicar cambios

    Aplica la estrategia seleccionada y actualiza el estado con los datos procesados y el flag de outliers manejados.
    Si no se detectan outliers, marca la etapa como completada sin modificar los datos.

    Parámetros:
    -----------
    estado : AppState
        Objeto que mantiene el estado global de la aplicación, incluyendo datos, columnas seleccionadas y flags de avance.

    Retorna:
    --------
    None
    """

    if not estado.normalizacion_completada:
        print(
            "❌ Error: Debe completar la normalización antes de detectar valores atípicos.")
        return

    # evaluaremos los outliers en columnas numericas y con valores únicos superiores a 2, así descartamos columnas binarias
    columnas_numericas = [
        col for col in estado.features
        if pd.api.types.is_numeric_dtype(estado.datos[col]) and estado.datos[col].nunique() > 2
    ]

    print("\n=============================")
    print("Detección y Manejo de Valores Atípicos")
    print("=============================")

    opciones = {
        "1": RemoveOutliers,
        "2": ReplaceOutliersWithMedian,
        "3": KeepOutliers,
        "4": None
    }

    # Vista previa de outliers
    temp_handler = RemoveOutliers(estado.datos, columnas_numericas)
    temp_handler.detect_outliers()
    if not temp_handler.outliers_info:
        print("✅ No se han detectado valores atípicos en las columnas seleccionadas.")
        estado.outliers_manejados = True
        return

    temp_handler.show_outliers_report()

    outlier = True
    while outlier:
        print("\nSeleccione una estrategia para manejar los valores atípicos:")
        print("  [1] Eliminar filas con valores atípicos")
        print("  [2] Reemplazar valores atípicos con la mediana de la columna")
        print("  [3] Mantener valores atípicos sin cambios")
        print("  [4] Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion in opciones and opcion != "4":
            handler = opciones[opcion](estado.datos, columnas_numericas)
            df_actualizado, completado = handler.execute()
            if completado:
                estado.datos = df_actualizado
                estado.outliers_manejados = True
            break
        elif opcion == "4":
            outlier = False
        else:
            print("Opción inválida.")
