import os
import pandas as pd
from unittest.mock import patch, MagicMock
from carga_datos import cargar_sqlite
from estado import AppState


# Mock para la entrada del archivo
@patch('builtins.input', return_value='dummy_path.sqlite')
@patch('sqlite3.connect')  # Mock para sqlite3.connect
def test_cargar_sqlite(mock_connect, mock_input):
    # Crear un mock para la conexión SQLite
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn

    # Simular la respuesta de las tablas en la base de datos
    # Simulamos que hay una tabla llamada 'table1'
    mock_cursor.fetchall.return_value = [('table1',)]

    # Crear un dataframe simulado para el mock de read_sql_query
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

    # Mock para pandas.read_sql_query
    with patch('pandas.read_sql_query', return_value=mock_df):
        # Instanciar AppState
        estado = AppState()

        # Llamar a la función que estamos probando
        cargar_sqlite(estado)

        # Verificar que el estado fue actualizado correctamente
        # Comprobar que los datos en el estado coinciden con el dataframe mockeado
        assert estado.datos.equals(mock_df)
        # Comprobar el nombre del archivo
        assert estado.nombre_archivo == 'dummy_path.sqlite - tabla: table1'
