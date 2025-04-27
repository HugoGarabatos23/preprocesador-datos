from estado import AppState
from categoricos.estrategias_categoricas.one_hot_encoding import OneHotEncoding
from categoricos.estrategias_categoricas.label_encoding import LabelEncoding


def mostrar_submenu_transformacion_categorica(estado: AppState):

    if not estado.columnas_seleccionadas() or not estado.faltantes_manejados:
        print("❌ Error: Debe seleccionar columnas y manejar nulos antes de transformar.")
        return

    df = estado.datos
    columnas_categoricas = [col for col in estado.features if df[col].dtype ==
                            "object" or df[col].dtype.name == "category"]
    print("\n=============================")
    print("Transformación de Datos Categóricos")
    print("=============================")

    if not columnas_categoricas:
        print("✅ No se han detectado columnas categóricas en las variables de entrada seleccionadas.")
        estado.transformacion_categorica = True
        return

    print("Se han detectado columnas categóricas en las variables seleccionadas:")
    for col in columnas_categoricas:
        print(f"  - {col}")

    estrategia = None
    transformacion = True
    while transformacion:
        print("\nSeleccione una estrategia de transformación:")
        print("  [1] One-Hot Encoding")
        print("  [2] Label Encoding")
        print("  [3] Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estrategia = OneHotEncoding()
        elif opcion == "2":
            estrategia = LabelEncoding()
        elif opcion == "3":
            transformacion = False
        else:
            print("Opción inválida.")
            continue

        if estrategia is not None:
            try:
                # Antes de transformar: advertir al usuario si algunas columnas tienen demasiados únicos
                columnas_categoricas_filtradas = []
                for col in columnas_categoricas:
                    n_unicos = df[col].nunique()
                    if n_unicos > 40:
                        print(
                            f"\n⚠️  Atención: La columna '{col}' tiene {n_unicos} valores únicos.")
                        print(
                            "   El One-Hot Encoding podría crear muchísimas columnas adicionales, lo cual "
                            "complicaría los siguientes pasos del pipeline.")
                        decision = input(
                            f"¿Desea incluir '{col}' en la transformación? (s/n): ").strip().lower()
                        if decision == "s":
                            columnas_categoricas_filtradas.append(col)
                        else:
                            print(
                                f"🔵 '{col}' será excluida de la transformación.")
                    else:
                        columnas_categoricas_filtradas.append(col)

                estado.datos = estrategia.transformar(
                    df, columnas_categoricas_filtradas)

                # Actualizar las features correctamente después de transformar
                # columnas despues del one-hot encoding
                columnas_actuales = set(estado.datos.columns)
                # columnas antes del one hot
                columnas_originales = set(df.columns)

                nuevas_columnas = columnas_actuales - columnas_originales

                # Mantener las columnas numéricas o no categóricas que ya eran features
                columnas_no_categoricas = [
                    col for col in estado.features if col not in columnas_categoricas]

                # Features actualizadas: antiguas no categóricas + columnas nuevas creadas por el OneHot
                estado.features = columnas_no_categoricas + \
                    list(nuevas_columnas)

                estado.transformacion_categorica = True
                print("✅ Transformación completada con éxito.\n")
            except Exception as e:
                print(f"❌ Error al aplicar la transformación: {e}")
            break
