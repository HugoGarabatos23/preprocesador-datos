import pytest
import pandas as pd
from unittest.mock import patch
from carga_datos.carga_datos import cargar_excel
from estado import AppState


@pytest.fixture
def app_state():
    return AppState()


@patch('builtins.input', side_effect=['dummy_path.xlsx', '1'])
@patch('pandas.ExcelFile')
@patch('pandas.read_excel')
def test_cargar_excel(mock_read_excel, mock_ExcelFile, mock_input, app_state):
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    mock_read_excel.return_value = mock_df

    mock_xls = mock_ExcelFile.return_value
    mock_xls.sheet_names = ['Sheet1']

    cargar_excel(app_state)

    assert app_state.datos.equals(mock_df)
    assert app_state.nombre_archivo == 'dummy_path.xlsx - hoja: Sheet1'
