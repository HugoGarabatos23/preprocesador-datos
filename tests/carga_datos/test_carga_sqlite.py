import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from carga_datos.carga_datos import cargar_sqlite
from estado import AppState


@pytest.fixture
def app_state():
    return AppState()


@patch('builtins.input', side_effect=['dummy_path.sqlite', '1'])
@patch('sqlite3.connect')
def test_cargar_sqlite(mock_connect, mock_input, app_state):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn

    mock_cursor.fetchall.return_value = [('table1',)]
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

    with patch('pandas.read_sql_query', return_value=mock_df):
        cargar_sqlite(app_state)

    assert app_state.datos.equals(mock_df)
    assert app_state.nombre_archivo == 'dummy_path.sqlite - tabla: table1'
