import pandas as pd
from normalizacion.estrategias_normalizacion.zscore_normalization import ZScoreNormalization
from estado import AppState
from unittest.mock import patch


# Simulamos que se elige la opción 2 (Z-score Normalization)
@patch('builtins.input', side_effect=['2'])
def test_z_score_normalization(mock_input):
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

    # Crear la estrategia de Z-Score Normalization
    estrategia = ZScoreNormalization()

    # Aplicar la normalización
    columnas_numericas = ['columna_numerica_1', 'columna_numerica_2']
    estado.datos = estrategia.aplicar(df, columnas_numericas)

    # Verificar que la media sea cercana a 0 y la desviación estándar sea cercana a 1
    assert abs(estado.datos['columna_numerica_1'].mean()
               ) < 0.01  # La media debe ser cercana a 0
    # La desviación estándar debe ser 1
    assert abs(estado.datos['columna_numerica_1'].std() - 1) < 0.01
    assert abs(estado.datos['columna_numerica_2'].mean()
               ) < 0.01  # La media debe ser cercana a 0
    # La desviación estándar debe ser 1
    assert abs(estado.datos['columna_numerica_2'].std() - 1) < 0.01

    print("✅ La normalización Z-Score se aplicó correctamente.")
