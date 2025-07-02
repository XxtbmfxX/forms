CREATE TABLE proveedor (
    id_proveedor SERIAL PRIMARY KEY,
    nombre_proveedor VARCHAR(100) NOT NULL,
    telefono_proveedor VARCHAR(30),
    correo_proveedor VARCHAR(100),
    direccion VARCHAR(200),
    activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE fardo (
    id_fardo SERIAL PRIMARY KEY,
    id_proveedor INT NOT NULL REFERENCES proveedor(id_proveedor),
    costo_total DECIMAL NOT NULL,
    costo_flete DECIMAL,
    cantidad_prendas_inicial INT NOT NULL,
    cantidad_prendas_actual INT,
    fecha_compra DATE NOT NULL,
    descripcion_fardo VARCHAR(200),
    estado VARCHAR(20)
);

CREATE TABLE calidad (
    id_calidad SERIAL PRIMARY KEY,
    calidad_estado VARCHAR(20) NOT NULL UNIQUE,
    descripcion VARCHAR(200)
);

CREATE TABLE categoria (
    id_categoria SERIAL PRIMARY KEY,
    nombre_categoria VARCHAR(100) NOT NULL UNIQUE,
    descripcion_categoria VARCHAR(200)
);

CREATE TABLE talla (
    id_talla SERIAL PRIMARY KEY,
    nombre_talla VARCHAR(20) NOT NULL UNIQUE,
    tipo_talla VARCHAR(20),
    orden_display INT
);

CREATE TABLE producto (
    id_producto SERIAL PRIMARY KEY,
    id_fardo INT NOT NULL REFERENCES fardo(id_fardo),
    id_calidad INT REFERENCES calidad(id_calidad),
    id_categoria INT NOT NULL REFERENCES categoria(id_categoria),
    id_talla INT NOT NULL REFERENCES talla(id_talla),
    nombre VARCHAR(100) NOT NULL,
    codigo_interno VARCHAR(50) UNIQUE,
    descripcion_producto VARCHAR(200) NOT NULL,
    calidad_producto VARCHAR(20),
    precio_costo DECIMAL NOT NULL,
    precio_original DECIMAL NOT NULL,
    precio_actual DECIMAL NOT NULL,
    estado VARCHAR(20),
    fecha_ingreso DATE NOT NULL,
    color VARCHAR(30),
    genero VARCHAR(20)
);

CREATE TABLE venta (
    id_venta SERIAL PRIMARY KEY,
    fecha_venta DATE NOT NULL,
    hora_venta TIME,
    total_venta DECIMAL NOT NULL,
    descuento_total DECIMAL,
    observaciones VARCHAR(200),
    vendedor VARCHAR(100)
);

CREATE TABLE detalle_venta (
    id_detalle SERIAL PRIMARY KEY,
    id_venta INT NOT NULL REFERENCES venta(id_venta),
    id_producto INT NOT NULL REFERENCES producto(id_producto),
    cantidad INT NOT NULL DEFAULT 1,
    precio_unitario DECIMAL NOT NULL,
    descuento_aplicado DECIMAL DEFAULT 0,
    metodo_pago VARCHAR(20)
);

CREATE TABLE devolucion_cambio (
    id_devolucion SERIAL PRIMARY KEY,
    id_detalle_venta INT NOT NULL REFERENCES detalle_venta(id_detalle),
    tipo_operacion VARCHAR(20),
    cantidad INT NOT NULL,
    fecha_operacion DATE NOT NULL,
    motivo VARCHAR(50),
    monto_devuelto DECIMAL,
    estado VARCHAR(20),
    observaciones VARCHAR(200)
);

CREATE TABLE detalle_cambio (
    id_detalle_cambio SERIAL PRIMARY KEY,
    id_devolucion INT NOT NULL REFERENCES devolucion_cambio(id_devolucion),
    id_producto_nuevo INT NOT NULL REFERENCES producto(id_producto),
    diferencia_precio DECIMAL
);

CREATE TABLE movimiento_inventario (
    id_movimiento SERIAL PRIMARY KEY,
    id_producto INT NOT NULL REFERENCES producto(id_producto),
    tipo_movimiento VARCHAR(20),
    cantidad INT NOT NULL,
    fecha_movimiento DATE NOT NULL,
    observaciones VARCHAR(200),
    id_venta INT REFERENCES venta(id_venta),
    id_devolucion INT REFERENCES devolucion_cambio(id_devolucion)
);