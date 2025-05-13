# tests/test_menu_opciones.py
import pytest
from unittest.mock import patch
from menu.menu_opciones import manejar_opcion
from estado import AppState


@pytest.fixture
def estado():
    return AppState()


def test_manejar_opcion_cargar_datos(estado):
    with patch("builtins.input", return_value="1"):
        resultado = manejar_opcion("1", estado)

    assert resultado is True


def test_manejar_opcion_datos_no_cargados(estado):
    with patch("builtins.input", return_value="2"):
        resultado = manejar_opcion("2", estado)

    assert "❌ No se han cargado datos" in str(resultado)
