class AppState:
    """
    Clase singleton que mantiene el estado global de la aplicación de preprocesamiento de datos.

    Esta clase almacena los datos cargados, las columnas seleccionadas para
    features y target, y el estado de cada etapa del pipeline:
    - Selección de columnas
    - Manejo de valores faltantes
    - Transformación categórica
    - Normalización
    - Detección y manejo de outliers
    - Visualización
    - Exportación

    Provee métodos para verificar si se han completado ciertas etapas, 
    para resetear columnas y para obtener el estado actual del preprocesamiento.
    """

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.iniciar_estado()

        return cls._instancia

    def datos_cargados(self):
        return self.datos is not None and not self.datos.empty

    def columnas_seleccionadas(self):
        return (
            self.datos_cargados()
            and self.features
            and self.target
            and self.target not in self.features
        )

    def reset_columnas(self):
        self.features = []
        self.target = None

    def resumen_columnas(self):
        if self.columnas_seleccionadas():
            return f"Features = {self.features}, Target = {self.target}"
        else:
            return "No se han seleccionado columnas de entrada/salida correctamente."

    def preprocesamiento_iniciado(self):
        return (
            self.estado_columnas_seleccionadas or
            self.faltantes_manejados or
            self.transformacion_categorica or
            self.normalizacion_completada or
            self.outliers_manejados
        )

    def preprocesado_completo(self):
        return (
            self.estado_columnas_seleccionadas and
            self.faltantes_manejados and
            self.transformacion_categorica and
            self.normalizacion_completada and
            self.outliers_manejados
        )

    def visualizacion_completa(self):
        return (
            self.dispersion or
            self.heatmap or
            self.resumen_estadistico or
            self.histograma
        )

    def exportacion_completa(self):
        return (
            self.formato_csv or
            self.formato_xlsx
        )

    def iniciar_estado(self):
        # Solo se asigna al iniciar la normalización, para comparar gráficamente
        self.datos = None
        self.datos_sin_normalizar = None
        self.nombre_archivo = None
        self.features = []
        self.target = None

        # Estados de preprocesamiento
        self.estado_columnas_seleccionadas = False
        self.faltantes_manejados = False
        self.transformacion_categorica = False
        self.normalizacion_completada = False
        self.outliers_manejados = False
        self.columnas_binarias = []
        self.columnas_codificadas = []

        # Estados de visualización
        self.dispersion = False
        self.heatmap = False
        self.resumen_estadistico = False
        self.histograma = False

        # Estados de exportación
        self.formato_csv = False
        self.formato_xlsx = False
