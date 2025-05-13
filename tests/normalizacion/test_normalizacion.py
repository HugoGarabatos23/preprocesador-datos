# tests/normalizacion/test_normalizacion.py
import pytest
import pandas as pd
from unittest.mock import patch
from normalizacion.estrategias_normalizacion.minmax_scaling import MinMaxScaling
from normalizacion.estrategias_normalizacion.zscore_normalization import ZScoreNormalization
from normalizacion.normalizacion import mostrar_submenu_normalizacion
from estado import AppState


@pytest.fixture
def estado():
    datos = {
        'columna_numerica_1': [1, 2, 3, 4, 5],
        'columna_numerica_2': [10, 20, 30, 40, 50],
        'columna_categorica': ['a', 'b', 'a', 'c', 'b']
    }
    df = pd.DataFrame(datos)

    estado = AppState()
    estado.datos = df
    estado.features = ['columna_numerica_1',
                       'columna_numerica_2', 'columna_categorica']
    estado.columnas_binarias = []
    estado.faltantes_manejados = True
    return estado


def test_mostrar_submenu_min_max(estado):
    with patch("builtins.input", side_effect=["1"]):
        mostrar_submenu_normalizacion(estado)

    assert 0 <= estado.datos['columna_numerica_1'].min() <= 1
    assert 0 <= estado.datos['columna_numerica_1'].max() <= 1
    assert 0 <= estado.datos['columna_numerica_2'].min() <= 1
    assert 0 <= estado.datos['columna_numerica_2'].max() <= 1


def test_mostrar_submenu_zscore(estado):
    with patch("builtins.input", side_effect=["2"]):
        mostrar_submenu_normalizacion(estado)

    assert abs(estado.datos['columna_numerica_1'].mean()) < 0.01
    assert abs(estado.datos['columna_numerica_1'].std() - 1) < 0.01
    assert abs(estado.datos['columna_numerica_2'].mean()) < 0.01
    assert abs(estado.datos['columna_numerica_2'].std() - 1) < 0.01


def test_min_max_scaling(estado):
    estrategia = MinMaxScaling()
    columnas_numericas = ['columna_numerica_1', 'columna_numerica_2']
    estado.datos = estrategia.aplicar(estado.datos, columnas_numericas)

    assert 0 <= estado.datos['columna_numerica_1'].min() <= 1
    assert 0 <= estado.datos['columna_numerica_1'].max() <= 1
    assert 0 <= estado.datos['columna_numerica_2'].min() <= 1
    assert 0 <= estado.datos['columna_numerica_2'].max() <= 1


def test_z_score_normalization(estado):
    estrategia = ZScoreNormalization()
    columnas_numericas = ['columna_numerica_1', 'columna_numerica_2']
    estado.datos = estrategia.aplicar(estado.datos, columnas_numericas)

    assert abs(estado.datos['columna_numerica_1'].mean()) < 0.01
    assert abs(estado.datos['columna_numerica_1'].std() - 1) < 0.01
    assert abs(estado.datos['columna_numerica_2'].mean()) < 0.01
    assert abs(estado.datos['columna_numerica_2'].std() - 1) < 0.01
