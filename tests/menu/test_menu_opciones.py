# test_menu_opciones.py
from unittest.mock import patch
from menu.menu_opciones import manejar_opcion
from estado import AppState


def test_manejar_opcion_cargar_datos():
    estado = AppState()
    with patch("builtins.input", return_value="1"):  # Simula que el usuario elige la opción 1
        resultado = manejar_opcion("1", estado)

    # Aquí debes verificar que la función manejar_opcion realiza lo que esperas,
    # como cargar los datos correctamente (esto dependerá de cómo implementes la carga)
    assert resultado is True  # Asegúrate de que el flujo sigue correctamente


def test_manejar_opcion_datos_no_cargados():
    estado = AppState()
    with patch("builtins.input", return_value="2"):  # Simula que el usuario elige la opción 2
        resultado = manejar_opcion("2", estado)

    # Verifica que la opción 2 no se pueda seleccionar si no se han cargado datos
    # O algo similar según tu implementación
    assert "❌ No se han cargado datos" in str(resultado)
