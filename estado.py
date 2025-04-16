class AppState:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.datos = None
            cls._instancia.nombre_archivo = None
        return cls._instancia

    def datos_cargados(self):
        return self.datos is not None
