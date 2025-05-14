import pytest
import pandas as pd
from estado import AppState
from nulos.manejo_nulos import EliminarFilas, RellenarConstante, RellenarMediana, RellenarModa, RellenarMedia

# ---------- FIXTURE DE ESTADO CON NULOS ----------


@pytest.fixture
def estado_con_datos():
    data = {
        'A': [1, 2, None, 4],
        'B': [None, 2, 3, 4],
        'C': [1, 2, 3, 4]
    }
    df = pd.DataFrame(data)
    estado = AppState()
    estado.datos = df
    estado.features = ['A', 'B']
    estado.target = 'C'
    estado.estado_columnas_seleccionadas = True
    return estado


# ---------- TESTS DE MANEJO DE NULOS ----------

def test_eliminar_filas(estado_con_datos):
    # Eliminar filas con nulos
    # Instanciamos sin argumentos ya que EliminarFilas no los requiere
    estrategia = EliminarFilas()
    estado_con_datos.datos = estrategia.aplicar(
        estado_con_datos.datos, estado_con_datos.features)
    df = estado_con_datos.datos
    assert df.isnull().sum().sum() == 0
    assert df.shape[0] == 2  # Solo deben quedar 2 filas sin nulos


def test_rellenar_media(estado_con_datos):
    # Rellenar nulos con la media
    estrategia = RellenarMedia()  # Instanciamos sin argumentos
    estado_con_datos.datos = estrategia.aplicar(
        estado_con_datos.datos, estado_con_datos.features)
    df = estado_con_datos.datos
    assert df['A'].isnull().sum() == 0
    assert df['B'].isnull().sum() == 0


def test_rellenar_mediana(estado_con_datos):
    # Rellenar nulos con la mediana
    estrategia = RellenarMediana()  # Instanciamos sin argumentos
    estado_con_datos.datos = estrategia.aplicar(
        estado_con_datos.datos, estado_con_datos.features)
    df = estado_con_datos.datos
    assert df.isnull().sum().sum() == 0


def test_rellenar_moda(estado_con_datos):
    # Rellenar nulos con la moda
    estrategia = RellenarModa()  # Instanciamos sin argumentos
    estado_con_datos.datos = estrategia.aplicar(
        estado_con_datos.datos, estado_con_datos.features)
    df = estado_con_datos.datos
    assert df.isnull().sum().sum() == 0


def test_rellenar_constante(estado_con_datos):
    # Rellenar nulos con un valor constante
    valor_constante = 0  # Valor constante para rellenar
    # Instanciamos pasando el valor constante
    estrategia = RellenarConstante(valor_constante)
    estado_con_datos.datos = estrategia.aplicar(
        estado_con_datos.datos, estado_con_datos.features)
    df = estado_con_datos.datos
    assert df.isnull().sum().sum() == 0
    # Al menos un 0 debería haberse introducido
    # Comprobamos que haya al menos un valor 0
    assert (df == valor_constante).sum().sum() >= 1
