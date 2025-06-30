import streamlit as st
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from .db import engine

def calidad_form():
    st.header("Ingreso de Calidad")
    with st.form("form_calidad"):
        calidad_estado = st.selectbox("Estado de Calidad", ["primera", "segunda", "premium"])
        descripcion = st.text_area("Descripción")
        submitted = st.form_submit_button("Guardar Calidad")
        if submitted:
            try:
                with engine.begin() as conn:
                    conn.execute(text("""
                        INSERT INTO calidad (calidad_estado, descripcion)
                        VALUES (:calidad_estado, :descripcion)
                    """), {"calidad_estado": calidad_estado, "descripcion": descripcion})
                st.success("Calidad guardada correctamente")
            except SQLAlchemyError as e:
                st.error(f"Error al guardar calidad: {e}")
