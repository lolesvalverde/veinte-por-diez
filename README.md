# veinte-por-diez

# ¡Bienvenid@s al **veinte por diez**! 

Esta es una aplicación web diseñada para aficionados del pádel que desean organizar torneos amateur de forma rápida, sencilla y sin complicaciones de registro.

## Estructura del Proyecto

El repositorio está estructurado en dos carpetas para facilitar la Integración Continua (CI):
- **`backend/`**: Contiene la lógica del servidor Flask, modelos de base de datos (`models.py`) y sus dependencias.
- **`frontend/`**: Contiene las vistas HTML (`templates/`) y los recursos de estilos e imágenes (`static/`).

## Requisitos Previos

- Python 3.10 o superior

## Configuración del Entorno de Desarrollo

Para configurar el entorno de ejecución, sigue estos pasos desde la carpeta raíz del proyecto (`veinte-por-diez`):

1. **Crear el entorno virtual:**
   ```bash
   python3 -m venv .venv
   ```

2. **Activar el entorno virtual:**
   - En macOS / Linux:
     ```bash
     source .venv/bin/activate
     ```
   - En Windows (PowerShell):
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - En Windows (CMD):
     ```cmd
     .venv\Scripts\activate.bat
     ```

3. **Instalar las dependencias del Backend:**
   ```bash
   pip install -r backend/requirements.txt
   ```

## Cómo Arrancar la Aplicación

Una vez configurado y activo el entorno virtual, puedes iniciar la aplicación ejecutando el siguiente comando desde la raíz del proyecto:

```bash
python backend/app.py
```

La aplicación se iniciará y estará disponible en tu navegador en la siguiente dirección:
[http://localhost:8500](http://localhost:8500)

