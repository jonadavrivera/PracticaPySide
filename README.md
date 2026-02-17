# Practica PySide6

## Descripción
Este proyecto es una práctica de desarrollo de interfaces gráficas utilizando PySide6, la biblioteca de Python para crear aplicaciones de escritorio. El objetivo es familiarizarse con los conceptos básicos de PySide.
utilizando el diseño de interfaces con el editor de Qt Designer y con código, el uso de manejo de eventos y la creación de widgets personalizados.

## Comandos para ejecutar el proyecto
### 🖥️ Windows

Asegúrate de estar en la carpeta raíz del proyecto Ejemplo: (`C:\Users\Usuario\Desktop\proyecto_pyside`).

```bash
# 1. Crear el entorno virtual
python -m venv env

# 2. Activar el entorno
# Si usas PowerShell y recibes error de permisos, ejecuta primero:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\env\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
python main.py

```

### macOS (Apple Silicon M3 Pro)

Abre tu terminal en la carpeta del proyecto.

```bash
# 1. Crear el entorno virtual
python3 -m venv env

# 2. Activar el entorno
source env/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
python3 main.py

```

---

## Diseño de Interfaz (Qt Designer)

El programa **Designer** se instala automáticamente junto con PySide6 dentro de tu entorno virtual. Es la herramienta que usamos para crear los archivos `.ui`.

### Ubicación y Ejecución

| Sistema | Ruta del Ejecutable (dentro del proyecto) | Comando de Ejecución |
| --- | --- | --- |
| **Windows** | `.\env\Lib\site-packages\PySide6\designer.exe` | `.\env\Lib\site-packages\PySide6\designer.exe` |
| **macOS** | `./env/lib/python3.x/site-packages/PySide6/Designer.app` | `open ./env/lib/python3.13/site-packages/PySide6/Designer.app` |

> **Tip para Mac:** En macOS, se tiene un comando desde la terminal, se activa con el entorno activado usando:
> `pyside6-designer`

---

## Estructura del proyecto
- `main.py`: Archivo principal que inicia la aplicación.
- `README.md`: Archivo de documentación del proyecto.
- `requirements.txt`: Archivo que lista las dependencias del proyecto.
