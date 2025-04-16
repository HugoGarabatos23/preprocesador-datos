class AppState:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.datos = None
            cls._instancia.nombre_archivo = None
            cls._instancia.features = []
            cls._instancia.target = None
        return cls._instancia

    def datos_cargados(self):
        return self.datos is not None
    
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