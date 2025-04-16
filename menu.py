# menu.py
from estado import AppState
import re

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
                if not self.estado.columnas_seleccionadas():
                    print("[-] 2. Preprocesado de datos (selección de columnas requerida)")
                else: 
                    print("[✓] 2. Preprocesado de datos (selección de columnas completada)")

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
            elif opcion == "2":
                self.mostrar_submenu_seleccion_columnas() 
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

    def mostrar_submenu_seleccion_columnas(self):
        if not self.estado.datos_cargados():
            print("Error: No se han cargado datos. Cargue un archivo primero.")
            return

        # Mostrar las columnas disponibles
        print("\n=============================")
        print("Selección de Columnas")
        print("=============================")
        print("Columnas disponibles en los datos:")
        
        columnas = list(self.estado.datos.columns)
        for i, col in enumerate(columnas, 1):
            print(f"  [{i}] {col}")
        
        # Solicitar al usuario que ingrese las columnas de entrada (features)
        # Repetimos hasta que el usuario ingrese features y target válidos
        correccion = False
        while not correccion:
        
            features_input = input("\nIngrese los números de las columnas de entrada (features), separados por comas: ").strip()
            # Verificamos que la entrada contenga solo números, comas y espacios
                    # Validar con regex
            if not re.fullmatch(r"[0-9,\s]+", features_input):
                print("❌ Error: Use solo números separados por comas. Ejemplo: 1,2,3")
                continue
            
            try:
                features_indices = [int(i.strip()) - 1 for i in features_input.split(",")]
                if any(i < 0 or i >= len(columnas) for i in features_indices):
                    print(" ❌Error: Uno o más índices están fuera de rango.")
                    continue
            
            
                features = [columnas[i] for i in features_indices]

                if not features:
                    print("⚠ Error: Debe seleccionar al menos una columna como feature.")
                    continue
            
                # Solicitar la columna de salida (target)
                target_input = input("\nIngrese el número de la columna de salida (target): ").strip()
                if not target_input.isdigit():
                    print("❌ Error: El target debe ser un número válido.")
                    continue
            

                target_index = int(target_input) - 1

                if target_index < 0 or target_index >= len(columnas):
                    print("❌ Error: Índice fuera de rango.")
                    continue
                
                
                target = columnas[target_index]

                if target in features:
                    print("⚠ Error: La columna de salida (target) no puede estar entre las features.")
                    continue

                # Almacenar selección
                self.estado.features = features
                self.estado.target = target

                # Confirmar selección
                print(f"\nSelección guardada: Features = {self.estado.features}, Target = {self.estado.target}")
                
                # Actualizar estado del menú principal
                self.estado.estado_columnas_seleccionadas = True
                correccion = True

            except Exception:
                print("⚠ Error: Entrada inesperado. Intente nuevamente.")

    

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
            
