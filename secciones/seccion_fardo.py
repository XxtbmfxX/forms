import streamlit as st
from sqlalchemy import text, SQLAlchemyError
from .db import engine

def fardo_form():
    st.header("Ingreso de Fardo")
    with st.form("form_fardo"):
        id_proveedor = st.number_input("ID Proveedor", min_value=1)
        costo_total = st.number_input("Costo Total", min_value=0)
        costo_flete = st.number_input("Costo Flete", min_value=0)
        cantidad_inicial = st.number_input("Cantidad Prendas Inicial", min_value=0)
        cantidad_actual = st.number_input("Cantidad Prendas Actual", min_value=0)
        fecha_compra = st.date_input("Fecha de Compra")
        descripcion = st.text_area("Descripción del Fardo")
        estado = st.selectbox("Estado", ["recibido", "procesado", "agotado"])
        submitted = st.form_submit_button("Guardar Fardo")
        if submitted:
            with engine.begin() as conn:
                conn.execute(text("""
                    INSERT INTO fardo (id_proveedor, costo_total, costo_flete, cantidad_prendas_inicial, cantidad_prendas_actual, fecha_compra, descripcion_fardo, estado)
                    VALUES (:id_proveedor, :costo_total, :costo_flete, :cantidad_inicial, :cantidad_actual, :fecha_compra, :descripcion, :estado)
                """), {"id_proveedor": id_proveedor, "costo_total": costo_total, "costo_flete": costo_flete, "cantidad_inicial": cantidad_inicial, "cantidad_actual": cantidad_actual, "fecha_compra": fecha_compra, "descripcion": descripcion, "estado": estado})
            st.success("Fardo guardado correctamente")
