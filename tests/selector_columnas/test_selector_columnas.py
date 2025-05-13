import pytest
from unittest.mock import patch
from estado import AppState
import pandas as pd
from selector_columnas.selector_columnas import mostrar_submenu_seleccion_columnas


@pytest.fixture
def estado_con_datos():
    # Crear un DataFrame de prueba
    datos = {
        'columna_numerica_1': [1, 2, 3, 4, 5],
        'columna_numerica_2': [10, 20, 30, 40, 50],
        'columna_categorica': ['a', 'b', 'a', 'c', 'b']
    }
    df = pd.DataFrame(datos)

    # Crear el estado y cargar los datos
    estado = AppState()
    estado.datos = df
    return estado


# Simulamos que el usuario selecciona las columnas 1 y 2 para features, y 3 para target
@patch('builtins.input', side_effect=['1,2', '3'])
def test_mostrar_submenu_seleccion_columnas_correcto(mock_input, estado_con_datos):
    estado = estado_con_datos

    # Llamar a la función de selección de columnas
    mostrar_submenu_seleccion_columnas(estado)

    # Verificar que las features y el target se hayan almacenado correctamente
    assert estado.features == ['columna_numerica_1', 'columna_numerica_2']
    assert estado.target == 'columna_categorica'
    assert estado.estado_columnas_seleccionadas is True
    print("✅ La selección de columnas se hizo correctamente.")


# Simulamos que el usuario selecciona columnas 1 y 2 para features, y 5 (fuera de rango) para target
@patch('builtins.input', side_effect=['1,2', '5'])
def test_mostrar_submenu_seleccion_columnas_target_fuera_de_rango(mock_input, estado_con_datos):
    estado = estado_con_datos

    # Llamar a la función de selección de columnas
    mostrar_submenu_seleccion_columnas(estado)

    # Verificar que el target no se haya actualizado
    assert estado.target != 'columna_categorica'
    assert estado.estado_columnas_seleccionadas is False
    print("✅ El sistema maneja correctamente el target fuera de rango.")


# Simulamos que el usuario selecciona columnas 1 y 2 para features, y 1 para target (lo mismo que un feature)
@patch('builtins.input', side_effect=['1,2', '1'])
def test_mostrar_submenu_seleccion_columnas_target_en_features(mock_input, estado_con_datos):
    estado = estado_con_datos

    # Llamar a la función de selección de columnas
    mostrar_submenu_seleccion_columnas(estado)

    # Verificar que el target no se haya actualizado
    assert estado.target != 'columna_numerica_1'
    assert estado.estado_columnas_seleccionadas is False
    print("✅ El sistema maneja correctamente el caso donde el target está en las features.")


# Simulamos una entrada incorrecta para el target
@patch('builtins.input', side_effect=['1,2', '3a'])
def test_mostrar_submenu_seleccion_columnas_target_no_numero(mock_input, estado_con_datos):
    estado = estado_con_datos

    # Llamar a la función de selección de columnas
    mostrar_submenu_seleccion_columnas(estado)

    # Verificar que no se haya cambiado la selección
    assert estado.features == []
    assert estado.target == ''
    assert estado.estado_columnas_seleccionadas is False
    print("✅ El sistema maneja correctamente el caso cuando el target no es un número.")


# Simulamos que el usuario selecciona las columnas 1 y 2, y un número de target fuera de rango (0)
@patch('builtins.input', side_effect=['1, 2', '0'])
def test_mostrar_submenu_seleccion_columnas_target_fuera_rango(mock_input, estado_con_datos):
    estado = estado_con_datos

    # Llamar a la función de selección de columnas
    mostrar_submenu_seleccion_columnas(estado)

    # Verificar que el target no se haya cambiado
    assert estado.target != 'columna_numerica_1'
    assert estado.estado_columnas_seleccionadas is False
    print("✅ El sistema maneja correctamente el caso cuando el target es fuera de rango (0).")


# Simulamos una selección válida
@patch('builtins.input', side_effect=['1, 2', '3'])
def test_mostrar_submenu_seleccion_columnas_datos_no_cargados(mock_input):
    # Crear el estado sin datos cargados
    estado = AppState()

    # Llamar a la función de selección de columnas
    mostrar_submenu_seleccion_columnas(estado)

    # Verificar que no se haya realizado ninguna acción
    assert estado.features == []
    assert estado.target == ''
    print("✅ El sistema maneja correctamente el caso cuando los datos no están cargados.")
