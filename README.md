# Proyecto de Formularios y Consultas SQL con Streamlit

## Requisitos
- Python 3.9+
- Docker (opcional, recomendado para base de datos)

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

