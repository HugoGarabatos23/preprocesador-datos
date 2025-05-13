import pytest
from unittest.mock import patch
import pandas as pd
from estado import AppState
from visualizacion.dispersion import DispersionPlot
from visualizacion.heatmap import Heatmap
from visualizacion.histogramas import Histograma
from visualizacion.resumen_estadistico import ResumenEstadistico


@pytest.fixture
def estado_con_datos_resumen():
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [1, 1, 2, 2],
        'D': ['a', 'b', 'b', 'a']
    }
    df = pd.DataFrame(data)

    estado = AppState()
    estado.datos = df
    estado.features = ['A', 'B', 'C', 'D']
    estado.target = 'B'
    estado.columnas_binarias = []
    estado.columnas_codificadas = []
    estado.resumen_estadistico = False
    estado.dispersion = False
    estado.histograma = False
    estado.heatmap = False
    return estado


# Test para DispersionPlot
@patch("builtins.print")
def test_dispersion_plot(mock_print, estado_con_datos_resumen):
    visualizacion = DispersionPlot()
    visualizacion.crear_visualizacion(estado_con_datos_resumen)

    mock_print.assert_any_call(
        "✅ Gráficos de dispersión comparativos generados correctamente.")
    assert estado_con_datos_resumen.dispersion is True


# Test para Heatmap
@patch("builtins.print")
def test_heatmap(mock_print, estado_con_datos_resumen):
    visualizacion = Heatmap()
    visualizacion.crear_visualizacion(estado_con_datos_resumen)

    mock_print.assert_any_call("✅ Heatmap generado exitosamente.")
    assert estado_con_datos_resumen.heatmap is True


# Test para Histograma
@patch("builtins.print")
def test_histograma(mock_print, estado_con_datos_resumen):
    visualizacion = Histograma()
    visualizacion.crear_visualizacion(estado_con_datos_resumen)

    mock_print.assert_any_call("✅ Histograma generado exitosamente.")
    assert estado_con_datos_resumen.histograma is True


# Test para ResumenEstadistico
@patch("builtins.print")
def test_resumen_estadistico(mock_print, estado_con_datos_resumen):
    visualizacion = ResumenEstadistico()
    visualizacion.crear_visualizacion(estado_con_datos_resumen)

    mock_print.assert_any_call("\n📊 Resumen Estadístico de los Datos")
    mock_print.assert_any_call("\n📈 Variables Numéricas:")
    mock_print.assert_any_call(" Media")
    mock_print.assert_any_call("\n Variables Categóricas:")
    mock_print.assert_any_call("\n Distribución de 'C':")
    assert estado_con_datos_resumen.resumen_estadistico is True
