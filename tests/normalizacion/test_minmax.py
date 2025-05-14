import pandas as pd
from normalizacion.estrategias_normalizacion.minmax_scaling import MinMaxScaling


def test_min_max_scaling():
    datos = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(datos)
    estrategia = MinMaxScaling()
    columnas = ['col1', 'col2']
    df_transformado = estrategia.aplicar(df, columnas)

    assert 0 <= df_transformado['col1'].min() <= 1
    assert 0 <= df_transformado['col1'].max() <= 1
    assert 0 <= df_transformado['col2'].min() <= 1
    assert 0 <= df_transformado['col2'].max() <= 1
