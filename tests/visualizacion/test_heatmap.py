import pytest
from unittest.mock import patch
from visualizacion.heatmap import Heatmap


@patch("builtins.print")
def test_heatmap_con_datos(mock_print, estado_con_datos):
    visualizacion = Heatmap()
    visualizacion.crear_visualizacion(estado_con_datos)

    # Verifica que se marcó el estado correctamente
    assert estado_con_datos.heatmap is True

    # Verifica que se imprimió el mensaje de éxito
    mock_print.assert_any_call("✅ Mapa de calor generado exitosamente.")


@patch("builtins.print")
def test_heatmap_sin_columnas_numericas(mock_print, estado_con_datos):
    # Forzar que no haya columnas numéricas válidas, las convertimos todas a string
    estado_con_datos.datos = estado_con_datos.datos.applymap(str)

    visualizacion = Heatmap()
    visualizacion.crear_visualizacion(estado_con_datos)

    # Verifica que se imprimió el mensaje de error
    mock_print.assert_any_call(
        "❌ No hay columnas numéricas adecuadas para crear un mapa de calor.")
