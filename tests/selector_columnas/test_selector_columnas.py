import pytest
from unittest.mock import patch, MagicMock
from selector_columnas.selector_columnas import mostrar_submenu_seleccion_columnas


@pytest.fixture
def estado_mock():
    estado = MagicMock()
    estado.datos_cargados.return_value = True
    estado.datos.columns = ["Edad", "Altura", "Peso", "Genero"]
    estado.estado_columnas_seleccionadas = False
    return estado


def test_flujo_valido_de_seleccion(estado_mock, capfd):
    inputs = ["1,2", "3"]
    with patch("builtins.input", side_effect=inputs):
        mostrar_submenu_seleccion_columnas(estado_mock)

    out, _ = capfd.readouterr()

    assert "Selección guardada" in out
    assert estado_mock.features == ["Edad", "Altura"]
    assert estado_mock.target == "Peso"
    assert estado_mock.estado_columnas_seleccionadas is True


def test_error_entrada_invalida_caracteres(estado_mock, capfd):
    inputs = ["a,b", "1,2", "4"]
    with patch("builtins.input", side_effect=inputs):
        mostrar_submenu_seleccion_columnas(estado_mock)

    out, _ = capfd.readouterr()
    assert "❌ Error: Use solo números separados por comas" in out
    assert "Selección guardada" in out


def test_error_target_repetido_en_features(estado_mock, capfd):
    # Primer intento inválido, luego correcto
    inputs = ["1,2", "2", "1,2", "3"]
    with patch("builtins.input", side_effect=inputs):
        mostrar_submenu_seleccion_columnas(estado_mock)

    out, _ = capfd.readouterr()
    assert "no puede estar entre las features" in out
    assert "Selección guardada" in out
    assert estado_mock.features == ["Edad", "Altura"]
    assert estado_mock.target == "Peso"


def test_indices_fuera_de_rango(estado_mock, capfd):
    inputs = ["1,99", "1,2", "3"]
    with patch("builtins.input", side_effect=inputs):
        mostrar_submenu_seleccion_columnas(estado_mock)

    out, _ = capfd.readouterr()
    assert "fuera de rango" in out
    assert "Selección guardada" in out


def test_datos_no_cargados():
    estado = MagicMock()
    estado.datos_cargados.return_value = False

    with patch("builtins.input") as mock_input:
        mostrar_submenu_seleccion_columnas(estado)
        mock_input.assert_not_called()
