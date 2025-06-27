-- 1. Esquema de tablas
CREATE TABLE IF NOT EXISTS proveedor (
  id_proveedor SERIAL PRIMARY KEY,
  nombre_proveedor VARCHAR(255) NOT NULL,
  telefono_proveedor VARCHAR(50),
  correo_proveedor VARCHAR(255),
  direccion VARCHAR(255),
  activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS calidad (
  id_calidad SERIAL PRIMARY KEY,
  calidad_estado VARCHAR(50) NOT NULL UNIQUE,
  descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS categoria (
  id_categoria SERIAL PRIMARY KEY,
  nombre_categoria VARCHAR(100) NOT NULL UNIQUE,
  descripcion_categoria VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS talla (
  id_talla SERIAL PRIMARY KEY,
  nombre_talla VARCHAR(50) NOT NULL UNIQUE,
  tipo_talla VARCHAR(50),
  orden_display INT
);

CREATE TABLE IF NOT EXISTS fardo (
  id_fardo SERIAL PRIMARY KEY,
  id_proveedor INT NOT NULL REFERENCES proveedor(id_proveedor),
  costo_total INT NOT NULL,
  costo_flete INT,
  cantidad_prendas_inicial INT NOT NULL,
  cantidad_prendas_actual INT,
  fecha_compra DATE NOT NULL,
  descripcion_fardo VARCHAR(255),
  estado VARCHAR(50) CHECK (estado IN ('recibido','procesado','agotado'))
);

CREATE TABLE IF NOT EXISTS producto (
  id_producto SERIAL PRIMARY KEY,
  id_fardo INT NOT NULL REFERENCES fardo(id_fardo),
  id_calidad INT REFERENCES calidad(id_calidad),
  id_categoria INT NOT NULL REFERENCES categoria(id_categoria),
  id_talla INT NOT NULL REFERENCES talla(id_talla),
  nombre VARCHAR(255) NOT NULL,
  codigo_interno VARCHAR(100) UNIQUE,
  descripcion_producto VARCHAR(255) NOT NULL,
  calidad_producto VARCHAR(50) CHECK (calidad_producto IN ('primera','segunda','premium')),
  precio_costo INT NOT NULL,
  precio_original INT NOT NULL,
  precio_actual INT NOT NULL,
  estado VARCHAR(50) CHECK (estado IN ('disponible','vendido','reservado','dañado')),
  fecha_ingreso DATE NOT NULL,
  color VARCHAR(50),
  genero VARCHAR(50) CHECK (genero IN ('hombre','mujer','unisex','niño'))
);

-- 2. Datos de prueba (hasta 5 por tabla)
INSERT INTO proveedor (nombre_proveedor, telefono_proveedor, correo_proveedor, direccion)
VALUES
  ('Prov A', '+56910000001', 'a@ejemplo.com', 'Av. Uno 1'),
  ('Prov B', '+56910000002', 'b@ejemplo.com', 'Calle Dos 2'),
  ('Prov C', '+56910000003', 'c@ejemplo.com', 'Camino Tres 3');

INSERT INTO calidad (calidad_estado, descripcion)
VALUES
  ('primera', 'Mayor calidad'),
  ('segunda', 'Calidad media'),
  ('premium', 'Calidad superior');

INSERT INTO categoria (nombre_categoria, descripcion_categoria)
VALUES
  ('Ropa', 'Prendas de vestir'),
  ('Calzado', 'Zapatos y similares'),
  ('Accesorio', 'Complementos varios');

INSERT INTO talla (nombre_talla, tipo_talla, orden_display)
VALUES
  ('S', 'ropa', 1),
  ('M', 'ropa', 2),
  ('L', 'ropa', 3),
  ('42', 'calzado', 1),
  ('43', 'calzado', 2);

INSERT INTO fardo (id_proveedor, costo_total, costo_flete, cantidad_prendas_inicial, cantidad_prendas_actual, fecha_compra, descripcion_fardo, estado)
VALUES
  (1, 1000, 100, 10, 10, '2025-06-01', 'Pedido inicial', 'recibido'),
  (2, 800, 80, 8, 8, '2025-06-05', 'Lote rápido', 'recibido');

INSERT INTO producto (id_fardo, id_calidad, id_categoria, id_talla, nombre, codigo_interno, descripcion_producto, calidad_producto, precio_costo, precio_original, precio_actual, estado, fecha_ingreso, color, genero)
VALUES
  (1, 1, 1, 1, 'Camiseta A', 'CMA100', 'Camiseta algodón', 'primera', 100, 150, 150, 'disponible', '2025-06-02', 'rojo', 'unisex'),
  (1, 2, 2, 4, 'Zapato B', 'ZPB200', 'Zapato deportivo', 'segunda', 200, 250, 250, 'disponible', '2025-06-03', 'negro', 'hombre');
