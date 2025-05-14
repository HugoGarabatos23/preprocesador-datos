import pytest
import pandas as pd
from unittest.mock import patch
from carga_datos.carga_datos import cargar_csv
from estado import AppState


@pytest.fixture
def app_state():
    return AppState()


@patch('builtins.input', return_value='dummy_path.csv')
@patch('pandas.read_csv')
def test_cargar_csv(mock_read_csv, mock_input, app_state):
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    mock_read_csv.return_value = mock_df

    cargar_csv(app_state)

    assert app_state.datos.equals(mock_df)
    assert app_state.nombre_archivo == 'dummy_path.csv'
