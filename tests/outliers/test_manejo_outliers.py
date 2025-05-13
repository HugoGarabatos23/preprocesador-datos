import pytest
import pandas as pd
from estado import AppState
from outliers.tratamiento_outliers.borrar_outliers import RemoveOutliers
from outliers.tratamiento_outliers.sustituir_outliers import ReplaceOutliersWithMedian
from outliers.tratamiento_outliers.mantener_outliers import KeepOutliers
from outliers.manejo_outliers import mostrar_submenu_manejo_outliers


# Crear un DataFrame de ejemplo
@pytest.fixture
def estado_con_datos():
    # Datos de ejemplo
    data = {
        'A': [1, 2, 3, 100],  # Outlier en A
        'B': [1, 2, 3, 4],
        'C': [1, 2, 3, 4]
    }
    df = pd.DataFrame(data)

    estado = AppState()
    estado.datos = df
    estado.features = ['A', 'B']
    estado.target = 'C'
    estado.estado_columnas_seleccionadas = True
    # Simula que la normalización ya está hecha
    estado.normalizacion_completada = True
    estado.outliers_manejados = False
    return estado

# Test para manejar outliers con el flujo completo


def test_manejo_outliers(estado_con_datos, capsys):
    # Ejecución de la función que maneja los outliers
    mostrar_submenu_manejo_outliers(estado_con_datos)

    # Capturamos la salida en consola
    captured = capsys.readouterr()

    # Comprobamos que el mensaje de no hay outliers detectados aparezca si es aplicable
    assert "No se han detectado valores atípicos" in captured.out or "Seleccionar una estrategia para manejar los valores atípicos" in captured.out

    # Probar que la opción 1 funciona (Eliminar outliers)
    # Simulamos la entrada del usuario para eliminar outliers
    # Esto puede cambiar dependiendo de la implementación de la opción en el flujo del menú
    # Aquí asumiendo que selecciona la opción 1.
    # Si ejecutamos el flujo con el capsys, podemos también verificar que la estrategia aplicada esté siendo mostrada en la salida.

    # Asegúrate de que el flujo está en su último estado
    estado_con_datos.datos = estado_con_datos.datos
    assert estado_con_datos.outliers_manejados is True


# Test para eliminar outliers (RemoveOutliers)
def test_remove_outliers(estado_con_datos):
    estrategia = RemoveOutliers(
        estado_con_datos.datos, estado_con_datos.features)
    df_resultado, _ = estrategia.execute()

    # Verifica que la fila con el outlier haya sido eliminada
    assert df_resultado.shape[0] == 3  # Debería quedar solo 3 filas
    assert df_resultado['A'].max() < 10  # El valor máximo de A no debe ser 100


# Test para reemplazar outliers con la mediana (ReplaceOutliersWithMedian)
def test_replace_outliers_with_median(estado_con_datos):
    estrategia = ReplaceOutliersWithMedian(
        estado_con_datos.datos, estado_con_datos.features)
    df_resultado, _ = estrategia.execute()

    # Verifica que el outlier ha sido reemplazado con la mediana
    assert df_resultado['A'].max() < 10  # El valor máximo de A no debe ser 100
    # El último valor debe ser la mediana, 2 en este caso
    assert df_resultado['A'].iloc[-1] == 2


# Test para mantener outliers (KeepOutliers)
def test_keep_outliers(estado_con_datos):
    estrategia = KeepOutliers(estado_con_datos.datos,
                              estado_con_datos.features)
    df_resultado, _ = estrategia.execute()

    # Verifica que el outlier no se haya tocado
    # El valor máximo de A debe seguir siendo 100
    assert df_resultado['A'].max() == 100
