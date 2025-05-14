from estado import AppState
from categoricos.estrategias_categoricas.one_hot_encoding import OneHotEncoding
from categoricos.estrategias_categoricas.label_encoding import LabelEncoding


def mostrar_submenu_transformacion_categorica(estado: AppState):
    """
    Muestra el submenú de transformación de datos categóricos.

    Esta función gestiona la interacción con el usuario para aplicar una estrategia
    de transformación sobre columnas categóricas de las variables de entrada.
    Permite seleccionar entre One-Hot Encoding y Label Encoding, aplicando la
    transformación elegida solo si se han seleccionado columnas y se han manejado
    previamente los valores nulos. También actualiza el estado de las columnas
    codificadas y las nuevas features generadas.

    Parámetros:
    - estado (AppState): Objeto que contiene el estado actual del pipeline,
      incluyendo los datos cargados, columnas seleccionadas y configuraciones.
    """

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
                # Filtrar las columnas categóricas que necesitan transformación
                columnas_categoricas_filtradas = []

                # Si la estrategia es One-Hot Encoding, pedimos confirmación para las columnas con más de 40 valores únicos
                if isinstance(estrategia, OneHotEncoding):
                    for col in columnas_categoricas:
                        n_unicos = df[col].nunique()
                        if n_unicos > 40:
                            print(
                                f"\n⚠️  Atención: La columna '{col}' tiene {n_unicos} valores únicos.")
                            print(
                                "   El One-Hot Encoding podría crear muchas columnas adicionales, lo cual complicaría los siguientes pasos.")
                            decision = input(
                                f"¿Desea incluir '{col}' en la transformación? (s/n): ").strip().lower()
                            if decision == "s":
                                columnas_categoricas_filtradas.append(col)
                            else:
                                print(
                                    f"🔵 '{col}' será excluida de la transformación.")
                        else:
                            columnas_categoricas_filtradas.append(col)

                # Si la estrategia es Label Encoding, no necesitamos la confirmación para las columnas
                elif isinstance(estrategia, LabelEncoding):
                    # Aplicamos Label Encoding a todas las categóricas sin excepción
                    columnas_categoricas_filtradas = columnas_categoricas
                    # Guardamos columnas codificadas (sobreescritas)
                    estado.columnas_codificadas = columnas_categoricas_filtradas

                # Aplicar la estrategia de transformación elegida
                estado.datos = estrategia.transformar(
                    df, columnas_categoricas_filtradas)

                # Actualizar las features después de la transformación
                columnas_actuales = set(estado.datos.columns)
                columnas_originales = set(df.columns)
                nuevas_columnas = columnas_actuales - columnas_originales

                # Mantener las columnas numéricas o no categóricas que ya eran features
                columnas_no_categoricas = [
                    col for col in estado.features if col not in columnas_categoricas]

                # Actualizamos las features con las nuevas columnas generadas por One-Hot Encoding (si aplica)
                estado.features = columnas_no_categoricas + \
                    list(nuevas_columnas)

                # Detectar y guardar las columnas binarias generadas por One-Hot Encoding, para no visualizarlas mas tarde
                columnas_binarias = [
                    col for col in nuevas_columnas
                    if set(estado.datos[col].unique()) <= {0, 1}
                ]
                estado.columnas_binarias = columnas_binarias

                estado.transformacion_categorica = True
                print("✅ Transformación completada con éxito.\n")

            except Exception as e:
                print(f"❌ Error al aplicar la transformación: {e}")
            break
