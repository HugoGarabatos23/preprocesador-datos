# tests/carga_datos/test_carga_datos.py
import pytest
from unittest.mock import patch, MagicMock
from carga_datos import mostrar_submenu_carga
from estado import AppState


@pytest.fixture
def app_state():
    return AppState()


@patch('builtins.input', side_effect=['s'])
@patch('carga_datos.AppState.datos_cargados', return_value=False)
def test_mostrar_submenu_carga_reiniciar(input_mock, datos_cargados_mock, app_state):
    # Comprobar que el submenu de carga maneja el reinicio cuando ya se ha iniciado el preprocesamiento
    mostrar_submenu_carga(app_state)
    app_state.iniciar_estado()
    input_mock.assert_called_once_with(
        "¿Desea reiniciar todo el proceso y cargar nuevos datos? [s/n]: ")
    assert app_state.datos is None  # El estado debe reiniciarse
