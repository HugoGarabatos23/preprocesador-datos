from estado import AppState

"""
Módulo encargado de renderizar el menú principal del pipeline de preprocesamiento.

Este módulo muestra el estado actual del flujo de trabajo, indicando visualmente qué
etapas están completas, pendientes o bloqueadas. Sirve como guía visual para que
el usuario entienda qué pasos puede realizar y en qué orden.
"""


def mostrar_menu_principal(estado: AppState):
    if estado.datos_cargados():
        print(f"[✓] 1. Cargar datos (archivo: {estado.nombre_archivo})")
    else:
        print("[-] 1. Cargar datos (ningún archivo cargado)")

    # Paso 2: Preprocesado
    if not estado.datos_cargados():
        print("[✗] 2. Preprocesado de datos (requiere carga de datos)")
    elif not estado.estado_columnas_seleccionadas:
        print("[-] 2. Preprocesado de datos (selección de columnas requerida)")
    else:
        print("[-] 2. Preprocesado de datos")

        if estado.estado_columnas_seleccionadas:
            print("      [✓] 2.1 Selección de columnas (completado)")
        else:
            print("      [-] 2.1 Selección de columnas (pendiente)")

        if estado.estado_columnas_seleccionadas and estado.faltantes_manejados:
            print("      [✓] 2.2 Manejo de datos faltantes (completado)")
        elif estado.estado_columnas_seleccionadas:
            print("      [-] 2.2 Manejo de datos faltantes (pendiente)")
        else:
            print(
                "      [✗] 2.2 Manejo de datos faltantes (requiere selección de columnas)")

        if estado.faltantes_manejados:
            print("      [✓] 2.3 Transformación de datos categóricos (completado)" if estado.transformacion_categorica else "      [-] 2.3 Transformación de datos categóricos (pendiente)")
        else:
            print(
                "      [✗] 2.3 Transformación de datos categóricos (requiere manejo de valores faltantes)")

        if estado.transformacion_categorica:
            print("      [✓] 2.4 Normalización y escalado (completado)" if estado.normalizacion_completada else "      [-] 2.4 Normalización y escalado (pendiente)")
        else:
            print(
                "      [✗] 2.4 Normalización y escalado (requiere transformación categórica)")

        if estado.normalizacion_completada:
            print("      [✓] 2.5 Detección y manejo de valores atípicos (completado)" if estado.outliers_manejados else "      [-] 2.5 Detección y manejo de valores atípicos (pendiente)")
        else:
            print(
                "      [✗] 2.5 Detección y manejo de valores atípicos (requiere normalización)")

    # Paso 3: Visualización
    if estado.visualizacion_completa():
        print("[✓] 3. Visualización de datos")
    elif estado.preprocesado_completo():
        print("[-] 3. Visualización de datos (pendiente)")
    else:
        print("[✗] 3. Visualización de datos (requiere preprocesado completo)")

    # Paso 4: Exportar
    if estado.exportacion_completa():
        print("[✓] 4. Exportar datos (completado)")

    elif estado.visualizacion_completa():
        print("[-] 4. Exportar datos")
    else:
        print("[✗] 4. Exportar datos (requiere preprocesado completo)")

    # Salir
    print("[✓] 5. Salir")
