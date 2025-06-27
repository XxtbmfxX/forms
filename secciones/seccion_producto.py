import streamlit as st
from sqlalchemy import text, SQLAlchemyError
from .db import engine

def producto_form():
    st.header("Ingreso de Producto")
    with engine.connect() as conn:
        fardos = conn.execute(text("SELECT id_fardo FROM fardo")).fetchall()
        calidades = conn.execute(text("SELECT id_calidad, calidad_estado FROM calidad")).fetchall()
        categorias = conn.execute(text("SELECT id_categoria, nombre_categoria FROM categoria")).fetchall()
        tallas = conn.execute(text("SELECT id_talla, nombre_talla FROM talla")).fetchall()

    fardo_opt = {f"Fardo {f[0]}": f[0] for f in fardos} if fardos else {"Sin fardos": None}
    calidad_opt = {c[1]: c[0] for c in calidades} if calidades else {"Sin calidades": None}
    categoria_opt = {c[1]: c[0] for c in categorias} if categorias else {"Sin categorías": None}
    talla_opt = {t[1]: t[0] for t in tallas} if tallas else {"Sin tallas": None}

    with st.form("form_producto"):
        id_fardo = st.selectbox("Fardo", options=list(fardo_opt.keys()))
        id_calidad = st.selectbox("Calidad", options=list(calidad_opt.keys()))
        id_categoria = st.selectbox("Categoría", options=list(categoria_opt.keys()))
        id_talla = st.selectbox("Talla", options=list(talla_opt.keys()))
        nombre = st.text_input("Nombre Producto")
        codigo = st.text_input("Código Interno")
        descripcion = st.text_area("Descripción")
        calidad_prod = st.selectbox("Calidad Producto", ["primera", "segunda", "premium"])
        precio_costo = st.number_input("Precio Costo", min_value=0)
        precio_original = st.number_input("Precio Original", min_value=0)
        precio_actual = st.number_input("Precio Actual", min_value=0)
        estado = st.selectbox("Estado", ["disponible", "vendido", "reservado", "dañado"])
        fecha_ingreso = st.date_input("Fecha Ingreso")
        color = st.text_input("Color")
        genero = st.selectbox("Género", ["hombre", "mujer", "unisex", "niño"])
        submitted = st.form_submit_button("Guardar Producto")
        if submitted:
            try:
                with engine.begin() as conn:
                    conn.execute(text("""
                        INSERT INTO producto (id_fardo, id_calidad, id_categoria, id_talla, nombre, codigo_interno, descripcion_producto, calidad_producto,
                        precio_costo, precio_original, precio_actual, estado, fecha_ingreso, color, genero)
                        VALUES (:id_fardo, :id_calidad, :id_categoria, :id_talla, :nombre, :codigo, :descripcion, :calidad_prod,
                        :precio_costo, :precio_original, :precio_actual, :estado, :fecha_ingreso, :color, :genero)
                    """), {
                        "id_fardo": fardo_opt[id_fardo],
                        "id_calidad": calidad_opt.get(id_calidad),
                        "id_categoria": categoria_opt[id_categoria],
                        "id_talla": talla_opt[id_talla],
                        "nombre": nombre,
                        "codigo": codigo,
                        "descripcion": descripcion,
                        "calidad_prod": calidad_prod,
                        "precio_costo": precio_costo,
                        "precio_original": precio_original,
                        "precio_actual": precio_actual,
                        "estado": estado,
                        "fecha_ingreso": fecha_ingreso,
                        "color": color,
                        "genero": genero
                    })
                st.success("Producto guardado correctamente")
            except SQLAlchemyError as e:
                st.error(f"Error al guardar producto: {e}")
