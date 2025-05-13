import pytest
from unittest.mock import patch
from estado import AppState
from categoricos.transformacion_categorica import mostrar_submenu_transformacion_categorica
import pandas as pd


@pytest.fixture
def estado():
    estado = AppState()
    estado.datos = pd.DataFrame({
        'columna_categorica': ['a', 'b', 'a', 'c', 'b'],
        'columna_numerica': [1, 2, 3, 4, 5]
    })
    estado.features = ['columna_categorica', 'columna_numerica']
    estado.faltantes_manejados = True
    return estado


@patch('builtins.input', side_effect=['1'])
def test_no_columnas_seleccionadas_o_nulos(mock_input, estado):
    estado.features = []
    estado.faltantes_manejados = False

    mostrar_submenu_transformacion_categorica(estado)

    assert "❌ Error: Debe seleccionar columnas y manejar nulos antes de transformar." in capsys.readouterr().out


@patch('builtins.input', side_effect=['2'])
def test_columnas_categoricas_detectadas(mock_input, estado):
    mostrar_submenu_transformacion_categorica(estado)

    assert "Se han detectado columnas categóricas en las variables seleccionadas:" in capsys.readouterr().out


def test_no_columnas_categoricas(estado):
    estado.datos = pd.DataFrame({
        'columna_numerica1': [1, 2, 3, 4, 5],
        'columna_numerica2': [6, 7, 8, 9, 10]
    })

    mostrar_submenu_transformacion_categorica(estado)

    assert estado.transformacion_categorica is True
    assert estado.columnas_codificadas == []
