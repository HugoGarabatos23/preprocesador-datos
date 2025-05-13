import pytest
import pandas as pd
from estado import AppState
from nulos.manejo_nulos import mostrar_submenu_manejo_nulos

# ---------- FIXTURE DE ESTADO CON NULOS ----------


@pytest.fixture
def estado_con_datos():
    data = {
        'A': [1, 2, None, 4],
        'B': [None, 2, 3, 4],
        'C': [1, 2, 3, 4]
    }
    df = pd.DataFrame(data)
    estado = AppState()
    estado.datos = df
    estado.features = ['A', 'B']
    estado.target = 'C'
    estado.estado_columnas_seleccionadas = True
    return estado


# ---------- TESTS DE INTEGRACIÓN CON EL MENÚ DE MANEJO DE NULOS ----------

def test_menu_eliminar_filas(monkeypatch, estado_con_datos):
    # Opción: eliminar filas
    monkeypatch.setattr("builtins.input", lambda _: "1")
    mostrar_submenu_manejo_nulos(estado_con_datos)
    df = estado_con_datos.datos
    assert df.isnull().sum().sum() == 0
    assert df.shape[0] == 2  # Solo deben quedar 2 filas sin nulos


def test_menu_rellenar_media(monkeypatch, estado_con_datos):
    # Opción: rellenar con media
    monkeypatch.setattr("builtins.input", lambda _: "2")
    mostrar_submenu_manejo_nulos(estado_con_datos)
    df = estado_con_datos.datos
    assert df['A'].isnull().sum() == 0
    assert df['B'].isnull().sum() == 0


def test_menu_rellenar_mediana(monkeypatch, estado_con_datos):
    # Opción: rellenar con mediana
    monkeypatch.setattr("builtins.input", lambda _: "3")
    mostrar_submenu_manejo_nulos(estado_con_datos)
    df = estado_con_datos.datos
    assert df.isnull().sum().sum() == 0


def test_menu_rellenar_moda(monkeypatch, estado_con_datos):
    # Opción: rellenar con moda
    monkeypatch.setattr("builtins.input", lambda _: "4")
    mostrar_submenu_manejo_nulos(estado_con_datos)
    df = estado_con_datos.datos
    assert df.isnull().sum().sum() == 0


def test_menu_rellenar_constante(monkeypatch, estado_con_datos):
    # Simula dos inputs: primero "5" para elegir rellenar constante, luego "0" como valor
    monkeypatch.setattr(
        "builtins.input", lambda msg: "5" if "nulo" in msg else "0")
    mostrar_submenu_manejo_nulos(estado_con_datos)
    df = estado_con_datos.datos
    assert df.isnull().sum().sum() == 0
    # Al menos un 0 debería haberse introducido
    assert (df == 0).sum().sum() >= 1


def test_menu_cancelar(monkeypatch, estado_con_datos):
    monkeypatch.setattr("builtins.input", lambda _: "0")  # Cancelar
    original = estado_con_datos.datos.copy()
    mostrar_submenu_manejo_nulos(estado_con_datos)
    pd.testing.assert_frame_equal(estado_con_datos.datos, original)


def test_menu_opcion_invalida(monkeypatch, estado_con_datos):
    monkeypatch.setattr("builtins.input", lambda _: "999")  # Opción inválida
    original = estado_con_datos.datos.copy()
    mostrar_submenu_manejo_nulos(estado_con_datos)
    pd.testing.assert_frame_equal(estado_con_datos.datos, original)
