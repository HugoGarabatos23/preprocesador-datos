import pytest
import pandas as pd
from unittest.mock import patch
from estado import AppState
from categoricos.transformacion_categorica import mostrar_submenu_transformacion_categorica
from categoricos.estrategias_categoricas.one_hot_encoding import OneHotEncoding
from categoricos.estrategias_categoricas.label_encoding import LabelEncoding


# Fixture para el estado
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


# Test de mostrar el submenu de transformación categórica
@patch('builtins.input', side_effect=['1'])
def test_no_columnas_seleccionadas_o_nulos(mock_input, estado, capsys):
    estado.features = []
    estado.faltantes_manejados = False

    mostrar_submenu_transformacion_categorica(estado)

    assert "❌ Error: Debe seleccionar columnas y manejar nulos antes de transformar." in capsys.readouterr().out


@patch('builtins.input', side_effect=['2'])
def test_columnas_categoricas_detectadas(mock_input, estado, capsys):
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


# Test de One-Hot Encoding
@patch('builtins.input', side_effect=['1'])
def test_one_hot_encoding(mock_input, estado):
    # Crear la estrategia de OneHotEncoding
    estrategia = OneHotEncoding()

    # Aplicar la transformación
    columnas_categoricas = ['columna_categorica']
    estado.datos = estrategia.transformar(estado.datos, columnas_categoricas)

    # Verificar que las nuevas columnas fueron creadas correctamente
    assert 'columna_categorica_a' in estado.datos.columns
    assert 'columna_categorica_b' in estado.datos.columns
    assert 'columna_categorica_c' in estado.datos.columns

    # Verificar que la columna original fue eliminada
    assert 'columna_categorica' not in estado.datos.columns


# Test de Label Encoding
@patch('builtins.input', side_effect=['2'])
def test_label_encoding(mock_input, estado):
    # Crear la estrategia de Label Encoding
    estrategia = LabelEncoding()

    # Aplicar la transformación
    columnas_categoricas = ['columna_categorica']
    estado.datos = estrategia.transformar(estado.datos, columnas_categoricas)

    # Verificar que la columna categórica ha sido transformada a códigos numéricos
    # 'a' debe convertirse en 0
    assert estado.datos['columna_categorica'].iloc[0] == 0
    # 'b' debe convertirse en 1
    assert estado.datos['columna_categorica'].iloc[1] == 1
    # 'a' debe convertirse en 0
    assert estado.datos['columna_categorica'].iloc[2] == 0
