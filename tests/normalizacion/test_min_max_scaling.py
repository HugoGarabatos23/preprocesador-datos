import pandas as pd
from normalizacion.estrategias_normalizacion.minmax_scaling import MinMaxScaling
from estado import AppState
from unittest.mock import patch


# Simulamos que se elige la opción 1 (Min-Max Scaling)
@patch('builtins.input', side_effect=['1'])
def test_min_max_scaling(mock_input):
    # Crear datos de prueba con columnas numéricas
    datos = {
        'columna_numerica_1': [1, 2, 3, 4, 5],
        'columna_numerica_2': [10, 20, 30, 40, 50],
        'columna_categorica': ['a', 'b', 'a', 'c', 'b']
    }
    df = pd.DataFrame(datos)

    # Crear estado
    estado = AppState()
    estado.datos = df
    estado.features = ['columna_numerica_1',
                       'columna_numerica_2', 'columna_categorica']
    estado.columnas_binarias = []  # Aseguramos que no haya columnas binarias
    estado.faltantes_manejados = True  # Asegurar que los faltantes estén manejados

    # Crear la estrategia de Min-Max Scaling
    estrategia = MinMaxScaling()

    # Aplicar la normalización
    columnas_numericas = ['columna_numerica_1', 'columna_numerica_2']
    estado.datos = estrategia.aplicar(df, columnas_numericas)

    # Verificar que las columnas se han normalizado correctamente
    # El valor mínimo debe ser 0
    assert 0 <= estado.datos['columna_numerica_1'].min() <= 1
    # El valor máximo debe ser 1
    assert 0 <= estado.datos['columna_numerica_1'].max() <= 1
    # El valor mínimo debe ser 0
    assert 0 <= estado.datos['columna_numerica_2'].min() <= 1
    # El valor máximo debe ser 1
    assert 0 <= estado.datos['columna_numerica_2'].max() <= 1

    print("✅ La normalización Min-Max Scaling se aplicó correctamente.")
