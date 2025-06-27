import streamlit as st
from sqlalchemy import text, SQLAlchemyError
from .db import engine

def categoria_form():
    st.header("Ingreso de Categoría")
    with st.form("form_categoria"):
        nombre_categoria = st.text_input("Nombre de la Categoría")
        descripcion_categoria = st.text_area("Descripción de la Categoría")
        submitted = st.form_submit_button("Guardar Categoría")
        if submitted:
            try:
                with engine.begin() as conn:
                    conn.execute(text("""
                        INSERT INTO categoria (nombre_categoria, descripcion_categoria)
                        VALUES (:nombre_categoria, :descripcion_categoria)
                    """), {"nombre_categoria": nombre_categoria, "descripcion_categoria": descripcion_categoria})
                st.success("Categoría guardada correctamente")
            except SQLAlchemyError as e:
                st.error(f"Error al guardar categoría: {e}")
