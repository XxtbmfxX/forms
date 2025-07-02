# app.py


import streamlit as st
from secciones.seccion_proveedor import proveedor_form
from secciones.seccion_fardo import fardo_form
from secciones.seccion_producto import producto_form
from secciones.seccion_calidad import calidad_form
from secciones.seccion_categoria import categoria_form
from secciones.seccion_talla import talla_form




st.sidebar.title("Navegación")
section = st.sidebar.radio(
    label="Seleccione una sección",
    options=["Proveedor", "Fardo", "Producto", "Categoría", "Talla", "Consultas"],
    label_visibility="collapsed"
)


if section == "Proveedor":
    proveedor_form()
elif section == "Fardo":
    fardo_form()
elif section == "Producto":
    producto_form()
elif section == "Calidad":
    calidad_form()
elif section == "Categoría":
    categoria_form()
elif section == "Talla":
    talla_form()
elif section == "Consultas":
    from secciones.seccion_consultas import consultas_sql_form
    consultas_sql_form()
