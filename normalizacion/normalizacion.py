import pandas as pd
from estado import AppState
from normalizacion.estrategias_normalizacion.minmax_scaling import MinMaxScaling
from normalizacion.estrategias_normalizacion.zscore_normalization import ZScoreNormalization


def mostrar_submenu_normalizacion(estado: AppState):
    if not estado.columnas_seleccionadas() or not estado.transformacion_categorica:
        print("❌ Error: Debe completar los pasos anteriores antes de normalizar.")
        return

    df = estado.datos
    columnas_numericas = [
        col for col in estado.features
        if pd.api.types.is_numeric_dtype(df[col]) and not pd.api.types.is_bool_dtype(df[col])
    ]

    # Verificar si existen columnas booleanas generadas por One-Hot Encoding
    columnas_booleanas = [
        col for col in estado.features if df[col].dtype == 'bool']
    if columnas_booleanas:
        print("⚠️  Recordatorio :  Las columnas binarias o generadas por One-Hot Encoding no se normalizarán, ya que sus valores son binarios (0 o 1) y no requieren normalización.")

    print("\n=============================")
    print("Normalización y Escalado")
    print("=============================")

    if not columnas_numericas:
        print("✅ No se han detectado columnas numéricas en las variables seleccionadas.")
        estado.normalizacion_completada = True
        return

    print("Se han detectado columnas numéricas en las variables seleccionadas:")
    for col in columnas_numericas:
        print(f"  - {col}")

    # Guardar los datos antes de cualquier normalización de cara al gráfico de dispersión
    estado.datos_sin_normalizar = df.copy()

    estrategia = None
    normalizacion = True
    while normalizacion:
        print("\nSeleccione una estrategia de normalización:")
        print("  [1] Min-Max Scaling (escala valores entre 0 y 1)")
        print("  [2] Z-score Normalization (media 0, desviación estándar 1)")
        print("  [3] Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estrategia = MinMaxScaling()
        elif opcion == "2":
            estrategia = ZScoreNormalization()
        elif opcion == "3":
            normalizacion = False
        else:
            print("Opción inválida.")
            continue

        if estrategia is not None:
            try:
                estado.datos = estrategia.aplicar(df, columnas_numericas)
                estado.normalizacion_completada = True
                print("✅ Normalización completada con éxito.\n")
            except Exception as e:
                print(f"❌ Error al aplicar la normalización: {e}")
            break
