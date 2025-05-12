class AppState:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.datos = None
            cls._instancia.datos_sin_normalizar = None
            cls._instancia.nombre_archivo = None
            cls._instancia.features = []
            cls._instancia.target = None

            # Inicializar estados de preprocesamiento
            cls._instancia.estado_columnas_seleccionadas = False
            cls._instancia.faltantes_manejados = False
            cls._instancia.transformacion_categorica = False
            cls._instancia.normalizacion_completada = False
            cls._instancia.outliers_manejados = False
            cls._instancia.columnas_binarias = []
            cls._instancia.columnas_codificadas = []

            # Inicializar estados de visualizacion
            cls._instancia.dispersion = False
            cls._instancia.heatmap = False
            cls._instancia.resumen_estadistico = False
            cls._instancia.histograma = False

            # Inicializar estados de exportacion
            cls._instancia.formato_csv = False
            cls._instancia.formato_xlsx = False

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
