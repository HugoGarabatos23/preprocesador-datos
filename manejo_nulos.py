# manejo_nulos.py

from estado import AppState
from estrategias_nulos.eliminar_filas import EliminarFilas
from estrategias_nulos.rellenar_media import RellenarMedia
from estrategias_nulos.rellenar_constante import RellenarConstante
from estrategias_nulos.rellenar_mediana import RellenarMediana
from estrategias_nulos.rellenar_moda import RellenarModa
# Puedes importar otras estrategias cuando las tengas

import pandas as pd

def mostrar_submenu_manejo_nulos(estado: AppState):
    if not estado.columnas_seleccionadas():
        print("❌ Error: Debe seleccionar columnas antes de manejar nulos.")
        return

 

    df = estado.datos
    columnas = estado.features + [estado.target]

    print("Columnas seleccionadas:", columnas)
    print("Columnas reales en df:", df.columns.tolist())

    # Detectar valores faltantes
    nulos = df[columnas].isnull().sum()
    print("\nResumen de valores nulos detectados en columnas seleccionadas:")
    print(nulos)
    print("\nCabin - valores nulos detectados:", df["Cabin"].isnull().sum())
    nulos_detectados = nulos[nulos > 0]

    print("\n=============================")
    print("Manejo de Valores Faltantes")
    print("=============================")

    if nulos_detectados.empty:
        print("✅ No se han detectado valores faltantes en las columnas seleccionadas.")
        estado.faltantes_manejados = True
        return

    print("Se han detectado valores faltantes en las siguientes columnas seleccionadas:")
    for col, cantidad in nulos_detectados.items():
        print(f"  - {col}: {cantidad} valores faltantes")

    menu_nulos = True
    while menu_nulos:
        print("\nSeleccione una estrategia para manejar los valores faltantes:")
        print("  [1] Eliminar filas con valores faltantes")
        print("  [2] Rellenar con la media de la columna")
        print("  [3] Rellenar con la mediana de la columna")
        print("  [4] Rellenar con la moda de la columna")
        print("  [5] Rellenar con un valor constante")
        print("  [6] Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estrategia = EliminarFilas()
        elif opcion == "2":
            estrategia = RellenarMedia()
        elif opcion == "3":
            estrategia = RellenarMediana()
        elif opcion == "4":
            estrategia = RellenarModa()
        elif opcion == "5":
            valor_input = input("Seleccione un valor constante para rellenar los nulos: ")
            try:
                # intenta convertir a número si es posible
                valor = float(valor_input) if valor_input.replace('.', '', 1).isdigit() else valor_input
                estrategia = RellenarConstante(valor)
            except ValueError:
                print("❌ Valor no válido.")
                continue
            
        elif opcion == "6":
            print("Volviendo al menú principal...")
            menu_nulos = False
            
        else:
            print("Opción inválida.")
            continue
    
        try:
            estado.datos = estrategia.aplicar(df, columnas)
            estado.faltantes_manejados = True
            print("✅ Valores faltantes gestionados correctamente.\n")
        except Exception as e:
            print(f"❌ Error al aplicar la estrategia: {e}")
        break

