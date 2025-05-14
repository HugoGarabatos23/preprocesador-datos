import pytest
from unittest.mock import patch
from visualizacion.resumen_estadistico import ResumenEstadistico


@patch("builtins.print")
def test_resumen_estadistico_excluyendo_transformadas(mock_print, estado_con_datos):
    estado_con_datos.target = "B"
    estado_con_datos.columnas_codificadas = ["A"]
    estado_con_datos.columnas_binarias = ["C"]

    visualizador = ResumenEstadistico()
    visualizador.crear_visualizacion(estado_con_datos)

    # Comprobamos que se menciona la exclusión
    mock_print.assert_any_call(
        "\n Se han excluido del resumen estadístico las siguientes columnas transformadas desde variables categóricas:")
    mock_print.assert_any_call(" Codificadas con Label Encoding: ['A']\n")
    mock_print.assert_any_call(
        " Generadas con One-Hot Encoding (columnas binarias): ['C']\n")

    assert estado_con_datos.resumen_estadistico is True
