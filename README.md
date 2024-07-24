# Proyecto de Análisis de Noticias

Este proyecto utiliza la API de NewsAPI para obtener las noticias más recientes de Argentina, procesa los datos y genera un informe en formato JSON.

## Requisitos Previos

- Python 3.7+
- Una clave de API válida para [NewsAPI](https://newsapi.org/). Puedes obtener una clave gratuita registrándote en su sitio web.

## Configuración

### 1. Crear un Entorno Virtual

Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto y evitar conflictos con otras bibliotecas instaladas globalmente.

```bash
python3 -m venv env

### 2. Activar el Entorno Virtual

Para activar el entorno virtual, usa el siguiente comando:

- En Linux/MacOS:

  ```bash
  source env/bin/activate


### 3. Instalar Dependencias

Una vez que el entorno virtual esté activo, instala las dependencias necesarias utilizando el archivo `requirements.txt`.

```bash
pip install -r requirements.txt


### 4. Configurar la Clave de API

Antes de ejecutar el script, asegúrate de configurar tu clave de API de NewsAPI. Puedes hacerlo de dos maneras:

1. **Editar el Script**: Añade tu clave de API directamente en el script `main.py` en la variable `API_KEY`.

### 5. Ejecutar el Script

Con las dependencias instaladas y la clave de API configurada, ejecuta el script para obtener y analizar los datos de noticias.

```bash
python app/main.py


### 6. Salida

El script generará un archivo `report.json` en el directorio de salida, que contendrá un resumen de los datos analizados.


Este `README.md` proporciona una guía clara para configurar el entorno, instalar dependencias, ejecutar el script y gestionar la clave de API. Puedes modificar los detalles según sea necesario para tu proyecto específico.
