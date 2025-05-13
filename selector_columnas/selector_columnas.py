from estado import AppState
import re


def mostrar_submenu_seleccion_columnas(estado: AppState) -> None:
    if not estado.datos_cargados():
        print("Error: No se han cargado datos. Cargue un archivo primero.")
        return

    # Mostrar las columnas disponibles
    print("\n=============================")
    print("Selección de Columnas")
    print("=============================")
    print("Columnas disponibles en los datos:")

    columnas = list(estado.datos.columns)
    for i, col in enumerate(columnas, 1):
        print(f"  [{i}] {col}")

    # Solicitar al usuario que ingrese las columnas de entrada (features)
    # Repetimos hasta que el usuario ingrese features y target válidos
    correccion = False
    while not correccion:

        features_input = input(
            "\nIngrese los números de las columnas de entrada (features), separados por comas: ").strip()
        # Verificamos que la entrada contenga solo números, comas y espacios
        # Validar con regex
        if not re.fullmatch(r"[0-9,\s]+", features_input):
            print("❌ Error: Use solo números separados por comas. Ejemplo: 1,2,3")
            continue

        try:
            features_indices = [
                int(i.strip()) - 1 for i in features_input.split(",")]
            if any(i < 0 or i >= len(columnas) for i in features_indices):
                print(" ❌Error: Uno o más índices están fuera de rango.")
                continue

            features = [columnas[i] for i in features_indices]

            if not features:
                print("⚠ Error: Debe seleccionar al menos una columna como feature.")
                continue

           # Solicitar la columna de salida (target)
            target_input = input(
                "\nIngrese el número de la columna de salida (target): ").strip()

            # Validar que sea un único número
            if not re.fullmatch(r"\d+", target_input):
                print(
                    "❌ Error: Solo se permite una única columna como target (un número).")
                continue

            target_index = int(target_input) - 1

            if target_index < 0 or target_index >= len(columnas):
                print("❌ Error: Índice fuera de rango.")
                continue

            target = columnas[target_index]

            if target in features:
                print(
                    "⚠ Error: La columna de salida (target) no puede estar entre las features.")
                continue

            # Almacenar selección
            estado.features = features
            estado.target = target

            # Confirmar selección
            print(
                f"\nSelección guardada: Features = {estado.features}, Target = {estado.target}")

            # Actualizar estado del menú principal
            estado.estado_columnas_seleccionadas = True
            correccion = True

        except Exception:
            print("⚠ Error: Entrada inesperado. Intente nuevamente.")
