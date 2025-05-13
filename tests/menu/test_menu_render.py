# tests/test_menu_render.py
import pytest
from unittest.mock import patch
from menu.menu_render import mostrar_menu_principal
from estado import AppState


@pytest.fixture
def estado():
    return AppState()


def test_mostrar_menu_principal_datos_cargados(estado):
    estado._datos = "archivo.csv"  # Simula que los datos están cargados

    with patch("builtins.print") as mock_print:
        mostrar_menu_principal(estado)

    mock_print.assert_any_call("[✓] 1. Cargar datos (archivo: archivo.csv)")


def test_mostrar_menu_principal_datos_no_cargados(estado):
    with patch("builtins.print") as mock_print:
        mostrar_menu_principal(estado)

    mock_print.assert_any_call("[-] 1. Cargar datos (ningún archivo cargado)")
