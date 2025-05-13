# test/exportacion/test_exportadores.py
import os
import pandas as pd
import pytest

from exportacion.tipos_exportacion.exportador_csv import ExportadorCSV
from exportacion.tipos_exportacion.exportador_excel import ExportadorExcel
from exportacion.exportador_factory import crear_exportador


@pytest.fixture
def df_ejemplo():
    return pd.DataFrame({
        "col1": [1, 2, 3],
        "col2": ["a", "b", "c"]
    })


def test_exportador_csv(df_ejemplo):
    exportador = ExportadorCSV()
    nombre_archivo = "test_salida_csv"
    ruta = f"{nombre_archivo}.csv"

    exportador.exportar(df_ejemplo, nombre_archivo)

    assert os.path.exists(ruta)
    df_leido = pd.read_csv(ruta)
    pd.testing.assert_frame_equal(df_ejemplo, df_leido)
    os.remove(ruta)


def test_exportador_excel(df_ejemplo):
    exportador = ExportadorExcel()
    nombre_archivo = "test_salida_excel"
    ruta = f"{nombre_archivo}.xlsx"

    exportador.exportar(df_ejemplo, nombre_archivo)

    assert os.path.exists(ruta)
    df_leido = pd.read_excel(ruta)
    pd.testing.assert_frame_equal(df_ejemplo, df_leido)
    os.remove(ruta)


def test_crear_exportador_csv():
    exportador = crear_exportador("1")
    assert isinstance(exportador, ExportadorCSV)


def test_crear_exportador_excel():
    exportador = crear_exportador("2")
    assert isinstance(exportador, ExportadorExcel)


def test_crear_exportador_invalido():
    exportador = crear_exportador("otra")
    assert exportador is None
