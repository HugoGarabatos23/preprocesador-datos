import pytest
from unittest.mock import patch
from visualizacion.histogramas import Histograma


@patch("builtins.print")
def test_histograma_con_datos(mock_print, estado_con_datos):
    visualizador = Histograma()
    visualizador.crear_visualizacion(estado_con_datos)

    assert estado_con_datos.histograma is True
    mock_print.assert_any_call("✅ Histograma generado exitosamente.")


@patch("builtins.print")
def test_histograma_sin_columnas_validas(mock_print, estado_con_datos):
    estado_con_datos.iniciar_estado()
    # Marcar todas las columnas como codificadas o binarias para que sean descartadas
    estado_con_datos.columnas_binarias = ['A', 'B']
    estado_con_datos.columnas_codificadas = ['C']

    visualizador = Histograma()
    visualizador.crear_visualizacion(estado_con_datos)

    mock_print.assert_any_call(
        "❌ No hay columnas numéricas adecuadas para crear un histograma.")
