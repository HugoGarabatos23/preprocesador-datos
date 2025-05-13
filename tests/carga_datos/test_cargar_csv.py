import os
import pandas as pd
from unittest.mock import patch
from carga_datos import cargar_csv
from estado import AppState


# Mock para la entrada del archivo
@patch('builtins.input', return_value='dummy_path.csv')
@patch('pandas.read_csv')  # Mock para la función read_csv
def test_cargar_csv(mock_read_csv, mock_input):
    # Crear un dataframe simulado para el mock de read_csv
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    # El mock de read_csv devuelve este dataframe
    mock_read_csv.return_value = mock_df

    # Instanciar AppState
    estado = AppState()

    # Llamar a la función que estamos probando
    cargar_csv(estado)

    # Verificar que el estado fue actualizado correctamente
    # Comprobar que los datos en el estado coinciden con el dataframe mockeado
    assert estado.datos.equals(mock_df)
    # Comprobar que el nombre del archivo fue actualizado correctamente
    assert estado.nombre_archivo == 'dummy_path.csv'
