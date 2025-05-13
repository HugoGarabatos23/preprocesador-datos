import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from carga_datos.carga_datos import mostrar_submenu_carga, cargar_csv, cargar_excel, cargar_sqlite
from estado import AppState


@pytest.fixture
def app_state():
    return AppState()

# Test para mostrar_submenu_carga y reiniciar el proceso


@patch('builtins.input', side_effect=['s'])
@patch('carga_datos.AppState.datos_cargados', return_value=False)
def test_mostrar_submenu_carga_reiniciar(input_mock, datos_cargados_mock, app_state):
    mostrar_submenu_carga(app_state)
    app_state.iniciar_estado()
    input_mock.assert_called_once_with(
        "¿Desea reiniciar todo el proceso y cargar nuevos datos? [s/n]: ")
    assert app_state.datos is None  # El estado debe reiniciarse

# Test para cargar_csv


@patch('builtins.input', return_value='dummy_path.csv')
@patch('pandas.read_csv')  # Mock para la función read_csv
def test_cargar_csv(mock_read_csv, mock_input, app_state):
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    mock_read_csv.return_value = mock_df

    cargar_csv(app_state)

    assert app_state.datos.equals(mock_df)
    assert app_state.nombre_archivo == 'dummy_path.csv'

# Test para cargar_excel


@patch('builtins.input', return_value='dummy_path.xlsx')
@patch('pandas.ExcelFile')  # Mock para la función ExcelFile
@patch('pandas.read_excel')  # Mock para la función read_excel
def test_cargar_excel(mock_read_excel, mock_ExcelFile, mock_input, app_state):
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    mock_read_excel.return_value = mock_df

    mock_xls = mock_ExcelFile.return_value
    mock_xls.sheet_names = ['Sheet1']

    cargar_excel(app_state)

    assert app_state.datos.equals(mock_df)
    assert app_state.nombre_archivo == 'dummy_path.xlsx - hoja: Sheet1'

# Test para cargar_sqlite


@patch('builtins.input', return_value='dummy_path.sqlite')
@patch('sqlite3.connect')  # Mock para sqlite3.connect
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
