import streamlit as st
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from .db import engine

def talla_form():
    st.header("Ingreso de Talla")
    with st.form("form_talla"):
        nombre_talla = st.text_input("Nombre de la Talla")
        tipo_talla = st.selectbox("Tipo de Talla", ["ropa", "calzado"])
        orden_display = st.number_input("Orden de Display", min_value=0)
        submitted = st.form_submit_button("Guardar Talla")
        if submitted:
            try:
                with engine.begin() as conn:
                    conn.execute(text("""
                        INSERT INTO talla (nombre_talla, tipo_talla, orden_display)
                        VALUES (:nombre_talla, :tipo_talla, :orden_display)
                    """), {"nombre_talla": nombre_talla, "tipo_talla": tipo_talla, "orden_display": orden_display})
                st.success("Talla guardada correctamente")
            except SQLAlchemyError as e:
                st.error(f"Error al guardar talla: {e}")
