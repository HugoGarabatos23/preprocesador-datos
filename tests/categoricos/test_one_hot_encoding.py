import pandas as pd
from categoricos.estrategias_categoricas.one_hot_encoding import OneHotEncoding


def test_one_hot_encoding_transforma_correctamente():
    df = pd.DataFrame({'animal': ['gato', 'perro', 'gato', 'pez']})
    transformado = OneHotEncoding().transformar(df, ['animal'])

    assert 'animal_gato' in transformado.columns
    assert 'animal_perro' in transformado.columns
    assert 'animal_pez' in transformado.columns
    assert 'animal' not in transformado.columns
