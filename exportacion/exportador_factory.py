# exportacion/exportador_factory.py
from exportacion.tipos_exportacion.exportador_csv import ExportadorCSV
from exportacion.tipos_exportacion.exportador_excel import ExportadorExcel


def crear_exportador(opcion: str):
    if opcion == "1":
        return ExportadorCSV()
    elif opcion == "2":
        return ExportadorExcel()
    else:
        return None
