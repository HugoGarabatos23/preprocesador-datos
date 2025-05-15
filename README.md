# Preprocesador de Datos CLI

Este proyecto es una herramienta interactiva de línea de comandos (CLI) para el preprocesamiento de datasets. Permite al usuario aplicar, paso a paso, operaciones comunes como:

- Carga de datos (`.csv`, `.xlsx`, `.db`, `.sqlite` )
- Selección de columnas (features y target)
- Manejo de valores faltantes
- Transformación de datos categóricos (One-Hot, Label Encoding)
- Normalización (Min-Max, Z-score)
- Detección y tratamiento de valores atípicos
- Visualización de datos antes y después del preprocesado
- Exportación de los datos procesados (`.csv`, `.xlsx`)

## Requisitos

- Python 3.12.2
- pip

## Instalación (descarga directa)

1. **Descarga el proyecto**

Ve a la sección de [Releases](https://github.com/HugoGarabatos23/preprocesador-datos/releases)  y descarga el archivo `.zip` más reciente o haz clic en el botón verde `Code` y luego en `Download ZIP` en la página principal del repositorio.

2. **Extrae el archivo ZIP**

Descomprime el archivo descargado en una carpeta local de tu elección.

3. **Crea un entorno virtual**

```bash
python -m venv venv
```
Activa el entorno virtual:
- En Windows
  
```bash
venv\Scripts\activate
```
- En macOS/Linux

```bash
source venv/bin/activate
```

4. **Instala los paquetes necesarios con:**

```bash
pip install -r requirements.txt
```

5. **Uso**
   
Sitúate en la carpeta en una consola y ejecuta

```bash
python main.py
```

##  Recomendación

Hacer uso de Visual Studio Code para una mejor experiencia de usuario

##  Inicio de navegación

El programa sigue la estructura de un pipeline. Está enfocado para seguir una serie de etapas secuencialmente. No se permite saltarse pasos. La única excepción es volver a cargar un nuevo archivo de datos sin tener que salir del programa.

 

![incio](https://github.com/user-attachments/assets/d85eb9c7-ea87-4415-8bd8-5fbffc4fa82b)

Para la ejecución del programa solo hará falta usar el teclado.
Aquí insertaremos la ruta correspondiente, si tenemos el archivo en la misma carpeta que el main.py reconocerá fácilmente  el archivo. 

![inicio2](https://github.com/user-attachments/assets/50539319-3b7e-43a2-a628-39beec5b3dac)

Durante el avance de las etapas irán surgiendo submenús para ampliar las opciones iniciales, de modo que tendremos varias maneras de procesar en cada etapa. Las etapas se van marcando como cerradas a medida que avanzamos, y abiertas en las que estemos. A mayores tenemos un mensaje en el menú que nos indica que pasos hacen falta para llegar a determinada acción.

![inicio3](https://github.com/user-attachments/assets/ba79b6af-723d-4385-a996-5b7db4c3ad07)

## Peculiaridad

Si volvemos a presionar en el menú inicial en número 1, nos saltará un mensaje de advertencia de que se perderá el progreso del pipeline y se podrá volver a empezar a gestionar otro archivo si se desea. Si escogemos seguir manejando nuestro archivo simplemente presionando  `n` seguiremos en el paso donde lo habíamos dejado.

![advertencia](https://github.com/user-attachments/assets/21642b7b-821c-4c1c-811c-08451dc22619)

## Pruebas 

Para ejecutar las pruebas hará solo falta ejecutar 


```bash
pytest
```


