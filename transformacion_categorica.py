from estado import AppState
from estrategias_categoricas.one_hot_encoding import OneHotEncoding
from estrategias_categoricas.label_encoding import LabelEncoding

def mostrar_submenu_transformacion_categorica(estado: AppState):
    

    if not estado.columnas_seleccionadas() or not estado.faltantes_manejados:
        print("❌ Error: Debe seleccionar columnas y manejar nulos antes de transformar.")
        return

    df = estado.datos
    columnas_categoricas = [col for col in estado.features if df[col].dtype == "object" or df[col].dtype.name == "category"]

    print("\n=============================")
    print("Transformación de Datos Categóricos")
    print("=============================")

    if not columnas_categoricas:
        print("✅ No se han detectado columnas categóricas en las variables de entrada seleccionadas.")
        estado.transformacion_categorica = True
        return

    print("Se han detectado columnas categóricas en las variables seleccionadas:")
    for col in columnas_categoricas:
        print(f"  - {col}")
    
    estrategia = None
    transformacion = True
    while transformacion:
        print("\nSeleccione una estrategia de transformación:")
        print("  [1] One-Hot Encoding")
        print("  [2] Label Encoding")
        print("  [3] Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estrategia = OneHotEncoding()
        elif opcion == "2":
            estrategia = LabelEncoding()
        elif opcion == "3":
            transformacion = False
        else:
            print("Opción inválida.")
            continue


        if estrategia is not None:
            try:
                estado.datos = estrategia.transformar(df, columnas_categoricas)
                # Actualizar features según las nuevas columnas del DataFrame 
                todas_columnas = set(estado.datos.columns)
                target = estado.target
                estado.features = list(todas_columnas - {target}) #target por separado
                estado.transformacion_categorica = True
                print("✅ Transformación completada con éxito.\n")
            except Exception as e:
                print(f"❌ Error al aplicar la transformación: {e}")
            break
