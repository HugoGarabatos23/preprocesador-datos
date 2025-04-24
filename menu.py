# menu.py
from estado import AppState
from menu_render import mostrar_menu_principal
from menu_opciones import manejar_opcion


class MenuManager:
    def __init__(self):
        self.estado = AppState()

    def menu_maestro(self):
        # Mostrar solo una vez al iniciar
        print("\nBienvenido al Preprocesador de Datos")
        print("=====================================")
        print("⚠️   Esta aplicación sigue un flujo de procesamiento paso a paso.")
        print("No es posible volver a etapas anteriores sin reiniciar pasos posteriores.")
        print("Asegúrese de sus selecciones en cada etapa.\n")
        seguir = True
        while seguir:
            mostrar_menu_principal(self.estado)
            opcion = input("Seleccione una opción: ")
            seguir = manejar_opcion(opcion, self.estado)

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
