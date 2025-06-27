
# 📄 Guía de Formularios en Streamlit

Streamlit permite crear formularios interactivos mediante `st.form`, lo que proporciona un mejor control sobre cuándo ejecutar acciones, ideal para insertar datos, hacer validaciones, etc.

---

## 🔹 ¿Qué es `st.form`?

`st.form` permite agrupar entradas (widgets) en un bloque que **no se ejecuta automáticamente** con cada cambio. Solo se ejecuta cuando el usuario hace clic en un botón de envío (`st.form_submit_button`).

---

## 🧱 Sintaxis Básica

```python
import streamlit as st

with st.form("formulario_articulo"):
    nombre = st.text_input("Nombre del artículo")
    precio = st.number_input("Precio", min_value=0.0, format="%.2f")
    categoria = st.selectbox("Categoría", ["Ropa", "Electrónica", "Hogar"])

    submit = st.form_submit_button("Guardar")

if submit:
    st.success(f"Artículo '{nombre}' guardado correctamente.")
```

---

## ✅ Características de `st.form`

| Elemento                  | Descripción |
|---------------------------|-------------|
| `st.form("id")`           | Crea el formulario con un ID único. |
| `st.form_submit_button()` | Obligatorio para ejecutar el formulario. |
| Widgets dentro del bloque | Se ejecutan solo al enviar el formulario. |

---

## 📥 Widgets Compatibles

Puedes incluir dentro de un formulario casi cualquier entrada, por ejemplo:

- `st.text_input()`
- `st.number_input()`
- `st.selectbox()`
- `st.slider()`
- `st.date_input()`
- `st.file_uploader()`

---

## 🛡️ Validaciones Básicas

```python
with st.form("login"):
    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")
    enviar = st.form_submit_button("Iniciar sesión")

if enviar:
    if not usuario or not clave:
        st.warning("Todos los campos son obligatorios.")
    else:
        st.success(f"Bienvenido, {usuario}")
```

---

## 📐 Formularios en Columnas

```python
with st.form("form_col"):
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre")
    with col2:
        edad = st.number_input("Edad", min_value=0)

    enviar = st.form_submit_button("Enviar")
```

---

## ⚖️ Diferencias con Widgets Fuera de Formularios

- **Fuera de `st.form`:** se ejecutan automáticamente al modificarse.
- **Dentro de `st.form`:** se ejecutan solo al presionar el botón de envío.

---

## 🧰 Casos de Uso Comunes

- Registro de usuarios o login
- Ingreso de productos o formularios complejos
- Inserciones en base de datos
- Validaciones múltiples

---

## 📚 Documentación Oficial

[https://docs.streamlit.io/library/api-reference/control-flow/st.form](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
