import pandas as pd
from categoricos.estrategias_categoricas.label_encoding import LabelEncoding


def test_label_encoding_transforma_correctamente():
    df = pd.DataFrame({'color': ['rojo', 'azul', 'rojo', 'verde']})
    transformado = LabelEncoding().transformar(df, ['color'])

    # Verifica que los valores ahora son enteros y consistentes
    assert set(transformado['color'].unique()).issubset({0, 1, 2})
    assert transformado['color'].dtype.kind in 'iu'  # integer/unsigned
