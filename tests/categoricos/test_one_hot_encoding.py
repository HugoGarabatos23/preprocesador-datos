import pytest
import pandas as pd
from unittest.mock import patch
from categoricos.estrategias_categoricas.one_hot_encoding import OneHotEncoding
from estado import AppState


@pytest.fixture
def datos_prueba():
    # Creamos un DataFrame de prueba para las transformaciones
    return pd.DataFrame({
        'columna_categorica': ['a', 'b', 'a', 'c', 'b'],
        'columna_numerica': [1, 2, 3, 4, 5]
    })


# Simulamos que se elige la opción 1 (One-Hot Encoding)
@patch('builtins.input', side_effect=['1'])
def test_one_hot_encoding(mock_input, datos_prueba):
    # Crear el estado
    estado = AppState()
    estado.datos = datos_prueba
    estado.features = ['columna_categorica', 'columna_numerica']
    estado.faltantes_manejados = True  # Asegurar que los faltantes estén manejados

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

    print("✅ La transformación One-Hot Encoding se aplicó correctamente.")

    # Verificar que las nuevas columnas fueron creadas correctamente
    assert 'columna_categorica_a' in estado.datos.columns
    assert 'columna_categorica_b' in estado.datos.columns
    assert 'columna_categorica_c' in estado.datos.columns

    # Verificar que la columna original fue eliminada
    assert 'columna_categorica' not in estado.datos.columns

    print("✅ La transformación One-Hot Encoding se aplicó correctamente.")
