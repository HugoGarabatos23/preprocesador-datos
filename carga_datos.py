# carga_datos.py

import pandas as pd
import sqlite3
import os
from estado import AppState


def mostrar_submenu_carga(estado: AppState) -> None:
    volver = False
    while not volver:
        print("\n=============================")
        print("Carga de Datos")
        print("=============================")
        print("Seleccione el tipo de archivo a cargar:")
        print("  [1] CSV")
        print("  [2] Excel")
        print("  [3] SQLite")
        print("  [4] Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cargar_csv(estado)
        elif opcion == "2":
            cargar_excel(estado)
        elif opcion == "3":
            cargar_sqlite(estado)
        elif opcion == "4":
            volver = True
        else:
            print("Opción inválida.")

        
        # Si la carga fue exitosa, volvemos automáticamente
        if estado.datos_cargados():
            return

def cargar_csv(estado):
    ruta = input("Ingrese la ruta del archivo CSV: ").strip()
    if not ruta.endswith(".csv"):
        print(" Error: El archivo no tiene extensión .csv")
        return

    try:
        df = pd.read_csv(ruta, sep=None, engine="python", na_values=["", " ", None, "NA", "N/A", "null"])  # detecta delimitador
        _mostrar_info(df)
        estado.datos = df
        estado.nombre_archivo = os.path.basename(ruta)
        print(" Datos cargados correctamente.\n")
    except Exception as e:
        print(f" Error al cargar el archivo CSV: {e}")

def cargar_excel(estado):
    ruta = input("Ingrese la ruta del archivo Excel (.xlsx): ").strip()
    if not ruta.endswith(".xlsx"):
        print(" Error: El archivo no tiene extensión .xlsx")
        return

    try:
        xls = pd.ExcelFile(ruta)
        print("Hojas disponibles:")
        for i, hoja in enumerate(xls.sheet_names, 1):
            print(f"  [{i}] {hoja}")
        eleccion = input("Seleccione una hoja por número: ").strip()
        hoja = xls.sheet_names[int(eleccion) - 1]
        df = pd.read_excel(xls, sheet_name=hoja)
        _mostrar_info(df)
        estado.datos = df
        estado.nombre_archivo = f"{os.path.basename(ruta)} - hoja: {hoja}"
        print(" Datos cargados correctamente.\n")
    except Exception as e:
        print(f" Error al cargar el archivo Excel: {e}")

def cargar_sqlite(estado):
    ruta = input("Ingrese la ruta de la base de datos SQLite: ").strip()
    if not (ruta.endswith(".sqlite") or ruta.endswith(".db")):
        print(" Error: El archivo debe tener xtensión .sqlite o .db")
        return

    try:
        conn = sqlite3.connect(ruta)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = [fila[0] for fila in cursor.fetchall()]

        if not tablas:
            print("No se encontraron tablas en la base de datos.")
            return

        print("Tablas disponibles en la base de datos:")
        for i, tabla in enumerate(tablas, 1):
            print(f"  [{i}] {tabla}")
        eleccion = input("Seleccione una tabla: ").strip()
        tabla = tablas[int(eleccion) - 1]

        df = pd.read_sql_query(f"SELECT * FROM {tabla}", conn)
        _mostrar_info(df)
        estado.datos = df
        estado.nombre_archivo = f"{os.path.basename(ruta)} - tabla: {tabla}"
        print(f"Datos de la tabla \"{tabla}\" cargados correctamente.\n")
    except Exception as e:
        print(f"Error al cargar datos desde SQLite: {e}")
    finally:
        conn.close()

def _mostrar_info(df):
    print("\nInformación del dataset:")
    print(f"Número de filas: {df.shape[0]}")
    print(f"Número de columnas: {df.shape[1]}")
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nPrimeras 5 filas:")
    print(df.head())
