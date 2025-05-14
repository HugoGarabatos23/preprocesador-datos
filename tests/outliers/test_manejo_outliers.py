import pytest
import pandas as pd
from outliers.tratamiento_outliers.borrar_outliers import RemoveOutliers
from outliers.tratamiento_outliers.sustituir_outliers import ReplaceOutliersWithMedian
from outliers.tratamiento_outliers.mantener_outliers import KeepOutliers

# ---------- FIXTURE CON OUTLIER CONTROLADO ----------


@pytest.fixture
def datos_con_outliers():
    data = {
        'A': [1, 2, 3, 100],  # 100 es un outlier
        'B': [1, 2, 3, 4]
    }
    df = pd.DataFrame(data)
    columnas = ['A', 'B']
    return df, columnas


# ---------- TEST RemoveOutliers ----------

def test_remove_outliers(datos_con_outliers):
    df, columnas = datos_con_outliers
    estrategia = RemoveOutliers(df, columnas)
    df_resultado, _ = estrategia.execute()

    assert df_resultado.shape[0] == 3  # Se elimina la fila con 100
    assert 100 not in df_resultado['A'].values


# ---------- TEST ReplaceOutliersWithMedian ----------

def test_replace_outliers_with_median(datos_con_outliers):
    df, columnas = datos_con_outliers
    estrategia = ReplaceOutliersWithMedian(df, columnas)
    df_resultado, _ = estrategia.execute()

    assert df_resultado.shape[0] == 4  # Ninguna fila se elimina
    assert 100 not in df_resultado['A'].values
    # Mediana de [1, 2, 3] es 2, y 100 debe haberse reemplazado por 2
    assert df_resultado['A'].iloc[-1] == 2


# ---------- TEST KeepOutliers ----------

def test_keep_outliers(datos_con_outliers):
    df, columnas = datos_con_outliers
    estrategia = KeepOutliers(df, columnas)
    df_resultado, _ = estrategia.execute()

    assert df_resultado.shape[0] == 4  # No se elimina nada
    assert 100 in df_resultado['A'].values  # Se conserva el outlier
