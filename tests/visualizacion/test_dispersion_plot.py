import pytest
from unittest.mock import patch
import pandas as pd
from estado import AppState
from visualizacion.dispersion import DispersionPlot


# Test para la creación de gráficos de dispersión cuando los datos son correctos
@patch("builtins.print")
def test_dispersion_plot_con_datos(mock_print, estado_con_datos):
    visualizacion = DispersionPlot()
    visualizacion.crear_visualizacion(estado_con_datos)

    # Verificar que el mensaje de éxito se imprimió
    mock_print.assert_any_call(
        "✅ Gráficos de dispersión comparativos generados correctamente.")
    assert estado_con_datos.dispersion is True


# Test cuando no hay datos originales para comparar
@patch("builtins.print")
def test_dispersion_plot_sin_datos(mock_print, estado_con_datos):
    estado_con_datos.datos_sin_normalizar = None  # No hay datos originales

    visualizacion = DispersionPlot()
    visualizacion.crear_visualizacion(estado_con_datos)

    # Verificar que se imprimió el mensaje de error
    mock_print.assert_any_call(
        "❌ No hay datos originales disponibles para comparar.")
