# menu.py
from estado import AppState
from menu.menu_render import mostrar_menu_principal
from menu.menu_opciones import manejar_opcion


class MenuManager:
    def __init__(self):
        self.estado = AppState()

    def menu_maestro(self):
        # Mostrar solo una vez al iniciar
        print("\nBienvenido al Preprocesador de Datos")
        print("=====================================")
        print("⚠️   Esta aplicación sigue un flujo de procesamiento paso a paso.")
        print("No es posible volver a etapas anteriores, excepto si se carga un archivo de nuevo, lo cual reiniciará el programa por completo.")
        print("Asegúrese de sus selecciones en cada etapa.\n")
        seguir = True
        while seguir:
            mostrar_menu_principal(self.estado)
            opcion = input("Seleccione una opción: ")
            seguir = manejar_opcion(opcion, self.estado)
