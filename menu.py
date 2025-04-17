# menu.py
from estado import AppState
from selector_columnas import mostrar_submenu_seleccion_columnas
from carga_datos import mostrar_submenu_carga
from manejo_nulos import mostrar_submenu_manejo_nulos



class MenuManager:
    def __init__(self):
        self.estado = AppState()

    def mostrar_menu_principal(self):
        seguir = True
        while seguir:
            print("\n=============================")
            print("Menú Principal")
            print("=============================")

            # Paso 1: Carga de datos
            if self.estado.datos_cargados():
                print(f"[✓] 1. Cargar datos (archivo: {self.estado.nombre_archivo})")
            else:
                print("[-] 1. Cargar datos (ningún archivo cargado)")

            # Paso 2: Preprocesado
            if not self.estado.datos_cargados():
                print("[✗] 2. Preprocesado de datos (requiere carga de datos)")
            elif not self.estado.estado_columnas_seleccionadas:
                print("[-] 2. Preprocesado de datos (selección de columnas requerida)")
            else:
                print("[-] 2. Preprocesado de datos")

                if self.estado.estado_columnas_seleccionadas:
                    print("      [✓] 2.1 Selección de columnas (completado)")
                else:
                    print("      [-] 2.1 Selección de columnas (pendiente)")

                if self.estado.estado_columnas_seleccionadas and self.estado.faltantes_manejados:
                    print("      [✓] 2.2 Manejo de datos faltantes (completado)")
                elif self.estado.estado_columnas_seleccionadas:
                    print("      [-] 2.2 Manejo de datos faltantes (pendiente)")
                else:
                    print("      [✗] 2.2 Manejo de datos faltantes (requiere selección de columnas)")

                if self.estado.faltantes_manejados:
                    print("      [✓] 2.3 Transformación de datos categóricos (completado)" if self.estado.transformacion_categorica else "      [-] 2.3 Transformación de datos categóricos (pendiente)")
                else:
                    print("      [✗] 2.3 Transformación de datos categóricos (requiere manejo de valores faltantes)")

                if self.estado.transformacion_categorica:
                    print("      [✓] 2.4 Normalización y escalado (completado)" if self.estado.normalizacion_completada else "      [-] 2.4 Normalización y escalado (pendiente)")
                else:
                    print("      [✗] 2.4 Normalización y escalado (requiere transformación categórica)")

                if self.estado.normalizacion_completada:
                    print("      [✓] 2.5 Detección y manejo de valores atípicos (completado)" if self.estado.outliers_manejados else "      [-] 2.5 Detección y manejo de valores atípicos (pendiente)")
                else:
                    print("      [✗] 2.5 Detección y manejo de valores atípicos (requiere normalización)")
                    

            # Paso 3: Visualización
            if self.estado.preprocesado_completo():
                print("[✓] 3. Visualización de datos")
            else:
                print("[✗] 3. Visualización de datos (requiere preprocesado completo)")

            # Paso 4: Exportar
            if self.estado.preprocesado_completo():
                print("[✓] 4. Exportar datos")
            else:
                print("[✗] 4. Exportar datos (requiere preprocesado completo)")

            # Salir
            print("[✓] 5. Salir")



            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                mostrar_submenu_carga(self.estado)
            elif opcion == "2":
                mostrar_submenu_seleccion_columnas(self.estado)
            elif opcion == "2.1":
                mostrar_submenu_seleccion_columnas(self.estado)
            elif opcion == "2.2":
                    if self.estado.columnas_seleccionadas():
                        mostrar_submenu_manejo_nulos(self.estado)
                    else: 
                        print("❌ Debe seleccionar columnas primero.")

            elif opcion == "5":
                if self.confirmar_salida():
                    print("Cerrando la aplicación...")
                    seguir = False
                else:
                    print("\nRegresando al menú principal...")
            else:
                print("Opción no disponible. Elija otra.")
             

    def confirmar_salida(self):
        print("\n=============================")
        print("Salir de la Aplicación")
        print("=============================")
        print("¿Está seguro de que desea salir?")
        print("  [1] Sí")
        print("  [2] No")
        while True:
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                return True
            elif opcion == "2":
                return False
            else:
                print("Opción inválida. Intente de nuevo.")
            
