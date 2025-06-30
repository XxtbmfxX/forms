import streamlit as st
from sqlalchemy import text
from .db import engine


def consultas_sql_form():
    st.header("Consultas SQL Personalizadas")
    st.write("Ingrese una consulta SQL para ejecutar sobre la base de datos. Solo SELECT permitido.")
    consulta = st.text_area("Consulta SQL", value="SELECT * FROM producto LIMIT 10;")
    ejecutar = st.button("Ejecutar Consulta")
    if ejecutar:
        if not consulta.strip().lower().startswith("select"):
            st.error("Solo se permiten consultas SELECT.")
            return
        try:
            with engine.connect() as conn:
                resultado = conn.execute(text(consulta))
                filas = resultado.fetchall()
                columnas = resultado.keys()
                if filas:
                    st.dataframe([dict(zip(columnas, fila)) for fila in filas])
                else:
                    st.info("La consulta no devolvió resultados.")
        except Exception as e:
            st.error(f"Error al ejecutar la consulta: {e}")
