# test_menu_render.py
from unittest.mock import patch
from menu.menu_render import mostrar_menu_principal
from estado import AppState


@patch("builtins.print")
def test_mostrar_menu_principal_datos_cargados(mock_print):
    estado = AppState()
    estado._datos = "archivo.csv"  # Simula que los datos están cargados

    mostrar_menu_principal(estado)

    # Verifica que el mensaje correcto se imprime cuando los datos están cargados
    mock_print.assert_any_call("[✓] 1. Cargar datos (archivo: archivo.csv)")


@patch("builtins.print")
def test_mostrar_menu_principal_datos_no_cargados(mock_print):
    estado = AppState()

    mostrar_menu_principal(estado)

    # Verifica que el mensaje correcto se imprime cuando los datos no están cargados
    mock_print.assert_any_call("[-] 1. Cargar datos (ningún archivo cargado)")
