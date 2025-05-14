from normalizacion.estrategias_normalizacion import minmax_scaling
import pytest
import pandas as pd
from estado import AppState
from normalizacion.estrategias_normalizacion.minmax_scaling import MinMaxScaling


@pytest.fixture
def estado_con_datos():
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [1, 1, 2, 2],
        'D': ['a', 'b', 'b', 'a'],
    }
    df_original = pd.DataFrame(data)

    estado = AppState()
    estado.features = ['A', 'B', 'C']
    estado.target = 'D'

    # Guardar copia sin normalizar
    estado.datos_sin_normalizar = df_original.copy()

    # Normalizar manualmente columnas numéricas
    normalizador = MinMaxScaling()
    df_normalizado = normalizador.aplicar(df_original, estado.features)
    df_normalizado[estado.target] = df_original[estado.target]

    estado.datos = df_normalizado
    estado.columnas_binarias = []
    estado.columnas_codificadas = []
    estado.heatmap = False

    return estado
