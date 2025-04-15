# menu.py
from estado import AppState

class MenuManager:
    def __init__(self):
        self.estado = AppState()

    def mostrar_menu_principal(self):
        seguir = True
        while seguir:
            print("=============================")
            print("Menú Principal")
            print("=============================")
            if self.estado.datos_cargados():
                print("[✓] 1. Cargar datos (archivo:", self.estado.nombre_archivo + ")")
                print("[-] 2. Preprocesado de datos (selección de columnas requerida)")
                print("[✗] 3. Visualización de datos (requiere preprocesado)")
                print("[✗] 4. Exportar datos (requiere preprocesado)")
            else:
                print("[-] 1. Cargar datos (ningún archivo cargado)")
                print("[✗] 2. Preprocesado de datos (requiere carga de datos)")
                print("[✗] 3. Visualización de datos (requiere carga y preprocesado)")
                print("[✗] 4. Exportar datos (requiere carga y preprocesado)")

            print("[✓] 5. Salir")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.mostrar_submenu_carga()
            elif opcion == "5":
                if self.confirmar_salida():
                    print("Cerrando la aplicación...")
                    seguir = False
                else:
                    print("\nRegresando al menú principal...")
            else:
                print("Opción no disponible. Elija otra.")

    def mostrar_submenu_carga(self):
        from carga_datos import cargar_csv, cargar_excel, cargar_sqlite
        volver = False
        while not volver:
            print("\n=============================")
            print("Carga de Datos")
            print("=============================")
            print("Seleccione el tipo de archivo a cargar:")
            print("  [1] CSV")
            print("  [2] Excel")
            print("  [3] SQLite")
            print("  [4] Volver al menú principal")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                cargar_csv(self.estado)
            elif opcion == "2":
                cargar_excel(self.estado)
            elif opcion == "3":
                cargar_sqlite(self.estado)
            elif opcion == "4":
                volver = True
            else:
                print("Opción inválida.")

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
            
