# exportacion/exportar_datos.py
from exportacion.exportador_factory import crear_exportador


def mostrar_submenu_exportacion(estado):
    if not estado.preprocesado_completo() or not estado.visualizacion_completa:
        print("❌ No es posible exportar los datos hasta completar el preprocesado y la visualización.")
        return

    expo = True
    while expo:

        print("\n=============================")
        print("Exportación de Datos")
        print("=============================")
        print("Seleccione el formato de exportación:")
        print("  [1] CSV (.csv)")
        print("  [2] Excel (.xlsx)")
        print("  [3] Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1" or opcion == "2":
            nombre_archivo = input(
                "Ingrese el nombre del archivo de salida (sin extensión): ").strip()
            exportador = crear_exportador(opcion)
            if exportador:
                try:
                    exportador.exportar(estado.datos, nombre_archivo)
                    print(
                        f" Datos exportados correctamente como '{nombre_archivo}.{exportador.extension}'")
                except Exception as e:
                    print(f"❌ Error al exportar los datos: {e}")

        elif opcion == "3":
            print(" Regresando al menú principal.")
            expo = False
