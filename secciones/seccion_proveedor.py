import streamlit as st
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from .db import engine

def proveedor_form():
    st.header("Ingreso de Proveedor")
    with st.form("form_proveedor"):
        nombre = st.text_input("Nombre del proveedor")
        telefono = st.text_input("Teléfono")
        correo = st.text_input("Correo")
        direccion = st.text_input("Dirección")
        activo = st.checkbox("Activo", value=True)
        submitted = st.form_submit_button("Guardar Proveedor")
        if submitted:
            if not nombre or not telefono or not correo or not direccion:
                st.warning("Todos los campos son obligatorios.")
            else:
                try:
                    with engine.begin() as conn:
                        conn.execute(text("""
                            INSERT INTO proveedor (nombre_proveedor, telefono_proveedor, correo_proveedor, direccion, activo)
                            VALUES (:nombre, :telefono, :correo, :direccion, :activo)
                        """), {"nombre": nombre, "telefono": telefono, "correo": correo, "direccion": direccion, "activo": activo})
                    st.success("Proveedor guardado correctamente")
                except SQLAlchemyError as e:
                    st.error(f"Error al guardar proveedor: {e}")
