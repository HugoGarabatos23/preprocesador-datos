# menu_opciones.py
from selector_columnas.selector_columnas import mostrar_submenu_seleccion_columnas
from carga_datos.carga_datos import mostrar_submenu_carga
from nulos.manejo_nulos import mostrar_submenu_manejo_nulos
from categoricos.transformacion_categorica import mostrar_submenu_transformacion_categorica
from normalizacion.normalizacion import mostrar_submenu_normalizacion
from outliers.manejo_outliers import mostrar_submenu_manejo_outliers
from visualizacion.visualizacion import Visualizacion


def manejar_opcion(opcion, estado):
    if opcion == "1":
        mostrar_submenu_carga(estado)
        estado.estado_columnas_seleccionadas = False

    elif opcion == "2" or opcion == "2.1":
        if not estado.datos_cargados():
            print(
                "❌ No se han cargado datos. Cargue un archivo antes de seleccionar columnas.")
        elif estado.estado_columnas_seleccionadas:
            print("⚠️  Las columnas ya han sido seleccionadas. No se puede volver atrás.")
        else:
            mostrar_submenu_seleccion_columnas(estado)

    elif opcion == "2.2":
        if estado.faltantes_manejados:
            print(
                "⚠️  Ya se ha completado el manejo de valores faltantes. Este paso no puede repetirse.")
        elif not estado.columnas_seleccionadas():
            print("❌ Debe seleccionar columnas primero.")
        else:
            mostrar_submenu_manejo_nulos(estado)

    elif opcion == "2.3":
        if not estado.faltantes_manejados:
            print(
                "❌ Error: Debe manejar los valores faltantes antes de transformar datos categóricos.")
        elif estado.transformacion_categorica:
            print("⚠️  Ya se completó la transformación de datos categóricos.")
        else:
            mostrar_submenu_transformacion_categorica(estado)

    elif opcion == "2.4":
        if estado.normalizacion_completada:
            print("⚠️  Ya se ha completado la normalización. No puede repetirse.")
        elif not estado.transformacion_categorica:
            print("❌ Debe completar la transformación categórica antes.")
        else:
            mostrar_submenu_normalizacion(estado)

    elif opcion == "2.5":
        if not estado.normalizacion_completada:
            print(
                "❌ Error: Debe completar la normalización antes de detectar valores atípicos.")
        elif estado.outliers_manejados:
            print("⚠️  Ya se completó la gestión de valores atípicos.")
        else:
            mostrar_submenu_manejo_outliers(estado)

    elif opcion == "3":
        if not estado.preprocesado_completo():
            print("❌ Completa el preprocesado antes de visualizar.")
        else:
            Visualizacion(estado.datos).mostrar_submenu()
            estado.visualizacion_completada = True

    elif opcion == "5":
        if not confirmar_salida():
            print("Cerrando la aplicación...")
            return False
        else:
            print("\nRegresando al menú principal...\n")

    else:
        print("Opción no disponible. Elija otra.")

    return True


def confirmar_salida():
    print("\n=============================")
    print("Salir de la Aplicación")
    print("=============================")
    print("¿Está seguro de que desea salir?")
    print("  [1] Sí")
    print("  [2] No")
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            return False
        elif opcion == "2":
            return True
        else:
            print("Opción inválida. Intente de nuevo.")
