import pandas as pd
from unittest.mock import patch
from estado import AppState
from categoricos.estrategias_categoricas.label_encoding import LabelEncoding


# Simulamos que se elige la opción 2 (Label Encoding)
@patch('builtins.input', side_effect=['2'])
def test_label_encoding(mock_input):
    # Crear datos de prueba con una columna categórica
    datos = {
        'columna_categorica': ['a', 'b', 'a', 'c', 'b'],
        'columna_numerica': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(datos)

    # Crear estado
    estado = AppState()
    estado.datos = df
    estado.features = ['columna_categorica', 'columna_numerica']
    estado.faltantes_manejados = True  # Asegurar que los faltantes estén manejados

    # Crear la estrategia de Label Encoding
    estrategia = LabelEncoding()

    # Aplicar la transformación
    columnas_categoricas = ['columna_categorica']
    estado.datos = estrategia.transformar(df, columnas_categoricas)

    # Verificar que la columna categórica ha sido transformada a códigos numéricos
    # 'a' debe convertirse en 0
    assert estado.datos['columna_categorica'].iloc[0] == 0
    # 'b' debe convertirse en 1
    assert estado.datos['columna_categorica'].iloc[1] == 1
    # 'a' debe convertirse en 0
    assert estado.datos['columna_categorica'].iloc[2] == 0

    print("✅ La transformación Label Encoding se aplicó correctamente.")
