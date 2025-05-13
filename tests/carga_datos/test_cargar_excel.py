import os
import pandas as pd
from unittest.mock import patch
from carga_datos import cargar_excel
from estado import AppState


# Mock para la entrada del archivo
@patch('builtins.input', return_value='dummy_path.xlsx')
@patch('pandas.ExcelFile')  # Mock para la función ExcelFile
@patch('pandas.read_excel')  # Mock para la función read_excel
def test_cargar_excel(mock_read_excel, mock_ExcelFile, mock_input):
    # Crear un dataframe simulado para el mock de read_excel
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    # El mock de read_excel devuelve este dataframe
    mock_read_excel.return_value = mock_df

    # Crear un mock para ExcelFile (simulando que tiene hojas)
    mock_xls = mock_ExcelFile.return_value
    # Simular que hay una hoja llamada 'Sheet1'
    mock_xls.sheet_names = ['Sheet1']

    # Instanciar AppState
    estado = AppState()

    # Llamar a la función que estamos probando
    cargar_excel(estado)

    # Verificar que el estado fue actualizado correctamente
    # Comprobar que los datos en el estado coinciden con el dataframe mockeado
    assert estado.datos.equals(mock_df)
    # Comprobar el nombre del archivo
    assert estado.nombre_archivo == 'dummy_path.xlsx - hoja: Sheet1'
