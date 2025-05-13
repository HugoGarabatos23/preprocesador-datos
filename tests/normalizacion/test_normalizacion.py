import pandas as pd
from normalizacion.estrategias_normalizacion.minmax_scaling import MinMaxScaling
from normalizacion.estrategias_normalizacion.zscore_normalization import ZScoreNormalization
from normalizacion.normalizacion import mostrar_submenu_normalizacion
from estado import AppState
from unittest.mock import patch


# Simulamos que se elige la opción 1 (Min-Max Scaling)
@patch('builtins.input', side_effect=['1'])
def test_mostrar_submenu_min_max(mock_input):
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

    # Llamar a la función mostrar_submenu_normalizacion
    mostrar_submenu_normalizacion(estado)

    # Verificar que la normalización se haya aplicado correctamente
    # El valor mínimo debe ser 0
    assert 0 <= estado.datos['columna_numerica_1'].min() <= 1
    # El valor máximo debe ser 1
    assert 0 <= estado.datos['columna_numerica_1'].max() <= 1
    # El valor mínimo debe ser 0
    assert 0 <= estado.datos['columna_numerica_2'].min() <= 1
    # El valor máximo debe ser 1
    assert 0 <= estado.datos['columna_numerica_2'].max() <= 1

    print("✅ La normalización Min-Max Scaling se aplicó correctamente desde el menú.")


# Simulamos que se elige la opción 2 (Z-Score Normalization)
@patch('builtins.input', side_effect=['2'])
def test_mostrar_submenu_zscore(mock_input):
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

    # Llamar a la función mostrar_submenu_normalizacion
    mostrar_submenu_normalizacion(estado)

    # Verificar que la normalización Z-Score se haya aplicado correctamente
    assert abs(estado.datos['columna_numerica_1'].mean()
               ) < 0.01  # La media debe ser cercana a 0
    # La desviación estándar debe ser 1
    assert abs(estado.datos['columna_numerica_1'].std() - 1) < 0.01
    assert abs(estado.datos['columna_numerica_2'].mean()
               ) < 0.01  # La media debe ser cercana a 0
    # La desviación estándar debe ser 1
    assert abs(estado.datos['columna_numerica_2'].std() - 1) < 0.01

    print("✅ La normalización Z-Score se aplicó correctamente desde el menú.")
