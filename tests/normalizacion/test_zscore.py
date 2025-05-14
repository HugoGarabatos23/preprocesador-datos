import pandas as pd
from normalizacion.estrategias_normalizacion.zscore_normalization import ZScoreNormalization


def test_z_score_normalization():
    datos = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(datos)
    estrategia = ZScoreNormalization()
    columnas = ['col1', 'col2']
    df_transformado = estrategia.aplicar(df, columnas)

    assert abs(df_transformado['col1'].mean()) < 0.01
    assert abs(df_transformado['col1'].std() - 1) < 0.01
    assert abs(df_transformado['col2'].mean()) < 0.01
    assert abs(df_transformado['col2'].std() - 1) < 0.01
