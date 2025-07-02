# Proyecto de Formularios y Consultas SQL con Streamlit

## Requisitos
- Python 3.9+
- Docker (opcional, recomendado para base de datos)



## Habilitar WSL 2 en Windows

Si usas Windows Home o necesitas WSL 2 para Docker Desktop, sigue estos pasos:

1. Abre PowerShell como administrador (clic derecho en el icono de PowerShell y selecciona "Ejecutar como administrador").
2. Habilita las características necesarias ejecutando:
   ```powershell
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```
3. Reinicia tu computadora.
4. Descarga el paquete de actualización de kernel de WSL 2 desde:
   [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel)
   e instálalo.
5. (Opcional) Si aún no tienes una distribución de Linux instalada, ejecuta en PowerShell:
   ```powershell
   wsl --install
   ```
   O instala una distribución desde Microsoft Store (por ejemplo, Ubuntu).
6. Establece WSL 2 como predeterminado:
   ```powershell
   wsl --set-default-version 2
   ```
7. Verifica que WSL 2 está activo con:
   ```powershell
   wsl --list --verbose
   ```

> **Nota:** Es posible que necesites actualizar Windows a una versión compatible (Windows 10 2004 o superior, Build 19041+).

---

## Instalación de Docker en Windows

Sigue estos pasos para instalar Docker Desktop en Windows:

1. Ve al sitio oficial de Docker: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Descarga el instalador para Windows.
3. Ejecuta el archivo descargado y sigue las instrucciones del asistente de instalación.
4. Cuando se te solicite, habilita la característica de virtualización en la BIOS si aún no está activa.
5. Finaliza la instalación y reinicia tu computadora si es necesario.
6. Inicia Docker Desktop desde el menú de inicio.
7. Espera a que el icono de Docker indique que está corriendo (puede tardar unos minutos la primera vez).
8. (Opcional) Inicia sesión con una cuenta de Docker Hub para acceder a imágenes públicas.

> **Nota:** Docker Desktop requiere Windows 10 64-bit: Pro, Enterprise o Education (Build 15063 o superior) o Windows 11. Para Windows Home, se requiere WSL 2.

---


## Crear y activar un entorno virtual para Python en Windows

Se recomienda usar un entorno virtual para aislar las dependencias del proyecto. Sigue estos pasos:

1. Abre una terminal (PowerShell o CMD) en la carpeta del proyecto.
2. Crea el entorno virtual ejecutando:
   ```powershell
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - En PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - En CMD:
     ```cmd
     .\venv\Scripts\activate.bat
     ```
4. Verifica que el entorno está activo: el prompt mostrará `(venv)` al inicio.
5. Instala las dependencias del proyecto:
   ```powershell
   pip install -r requirements.txt
   ```

---

## Instalación

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. (Opcional) Levanta la base de datos y PgAdmin con Docker:
   ```bash
   docker-compose up -d
   ```

3. Inicializa el esquema de la base de datos:
   - Puedes usar PgAdmin o psql para ejecutar `init_schema.sql` en la base de datos.

4. Ejecuta la app:
   ```bash
   streamlit run app.py
   ```

## Configuración

- Variables de entorno para la base de datos (opcional, ver `secciones/db.py` y `docker-compose.yml`):
  - `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, `POSTGRES_HOST`, `POSTGRES_PORT`

## Ejemplo de uso
- Ingresa datos en los formularios de la barra lateral.
- Realiza consultas SQL personalizadas en la sección "Consultas" (solo SELECT).

## Pruebas y Validación
- Se recomienda agregar scripts de prueba en el futuro (por ejemplo, usando `pytest`).
- Validaciones básicas y manejo de errores están implementados en los formularios.

## Documentación útil
- [Guía de formularios Streamlit](apuntes/guia_formularios_streamlit.md)
- [Documentación oficial Streamlit](https://docs.streamlit.io/)

