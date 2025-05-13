# tests/test_estado.py
import pytest
from estado import AppState


@pytest.fixture
def app_state():
    return AppState()


def test_singleton(app_state):
    # Verificar que siempre se obtiene la misma instancia
    app_state2 = AppState()
    assert app_state is app_state2


def test_datos_cargados(app_state):
    app_state.datos = "Algun dato"
    assert app_state.datos_cargados() is True
    app_state.datos = None
    assert app_state.datos_cargados() is False


def test_columnas_seleccionadas(app_state):
    app_state.datos = "Algun dato"
    app_state.features = ["feature1", "feature2"]
    app_state.target = "feature1"
    assert not app_state.columnas_seleccionadas()  # target está en features

    app_state.target = "feature3"
    assert app_state.columnas_seleccionadas()  # target no está en features


def test_reset_columnas(app_state):
    app_state.features = ["feature1"]
    app_state.target = "feature1"
    app_state.reset_columnas()
    assert app_state.features == []
    assert app_state.target is None


def test_resumen_columnas(app_state):
    app_state.features = ["feature1"]
    app_state.target = "feature2"
    assert app_state.resumen_columnas(
    ) == "Features = ['feature1'], Target = feature2"
    app_state.reset_columnas()
    assert app_state.resumen_columnas(
    ) == "No se han seleccionado columnas de entrada/salida correctamente."


def test_preprocesamiento_iniciado(app_state):
    app_state.estado_columnas_seleccionadas = True
    assert app_state.preprocesamiento_iniciado() is True
    app_state.estado_columnas_seleccionadas = False
    assert app_state.preprocesamiento_iniciado() is False


def test_preprocesado_completo(app_state):
    app_state.estado_columnas_seleccionadas = True
    app_state.faltantes_manejados = True
    app_state.transformacion_categorica = True
    app_state.normalizacion_completada = True
    app_state.outliers_manejados = True
    assert app_state.preprocesado_completo() is True
    app_state.outliers_manejados = False
    assert app_state.preprocesado_completo() is False


def test_visualizacion_completa(app_state):
    app_state.dispersion = True
    assert app_state.visualizacion_completa() is True
    app_state.dispersion = False
    assert app_state.visualizacion_completa() is False


def test_exportacion_completa(app_state):
    app_state.formato_csv = True
    assert app_state.exportacion_completa() is True
    app_state.formato_csv = False
    assert app_state.exportacion_completa() is False


def test_iniciar_estado(app_state):
    app_state.iniciar_estado()
    assert app_state.datos is None
    assert app_state.features == []
    assert app_state.target is None
    assert app_state.estado_columnas_seleccionadas is False
    assert app_state.faltantes_manejados is False
    assert app_state.transformacion_categorica is False
    assert app_state.normalizacion_completada is False
    assert app_state.outliers_manejados is False
    assert app_state.columnas_binarias == []
    assert app_state.columnas_codificadas == []
    assert app_state.dispersion is False
    assert app_state.heatmap is False
    assert app_state.resumen_estadistico is False
    assert app_state.histograma is False
    assert app_state.formato_csv is False
    assert app_state.formato_xlsx is False


def test_transiciones_estado_columnas_seleccionadas(app_state):
    # Verificamos que el estado de "columnas seleccionadas" comienza como False
    assert not app_state.estado_columnas_seleccionadas
    # Simulamos que se seleccionan las columnas
    app_state.estado_columnas_seleccionadas = True
    # Verificamos que el estado cambia a True
    assert app_state.estado_columnas_seleccionadas


def test_transiciones_faltantes_manejados(app_state):
    # Verificamos que el estado de "faltantes manejados" comienza como False
    assert not app_state.faltantes_manejados
    # Simulamos que se manejan los faltantes
    app_state.faltantes_manejados = True
    # Verificamos que el estado cambia a True
    assert app_state.faltantes_manejados


def test_transiciones_transformacion_categorica(app_state):
    # Verificamos que el estado de "transformación categórica" comienza como False
    assert not app_state.transformacion_categorica
    # Simulamos que se realiza la transformación categórica
    app_state.transformacion_categorica = True
    # Verificamos que el estado cambia a True
    assert app_state.transformacion_categorica


def test_transiciones_normalizacion_completada(app_state):
    # Verificamos que el estado de "normalización completada" comienza como False
    assert not app_state.normalizacion_completada
    # Simulamos que se completa la normalización
    app_state.normalizacion_completada = True
    # Verificamos que el estado cambia a True
    assert app_state.normalizacion_completada


def test_transiciones_outliers_manejados(app_state):
    # Verificamos que el estado de "outliers manejados" comienza como False
    assert not app_state.outliers_manejados
    # Simulamos que se manejan los outliers
    app_state.outliers_manejados = True
    # Verificamos que el estado cambia a True
    assert app_state.outliers_manejados
