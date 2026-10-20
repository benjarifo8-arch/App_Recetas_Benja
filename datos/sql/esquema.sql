CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL,
    contrasena TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS categorias (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_categoria TEXT NOT NULL,
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS recetas (
    id_receta INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    tiempo_preparacion INTEGER,
    dificultad TEXT,
    instrucciones TEXT,
    id_usuario INTEGER,
    id_categoria INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

CREATE TABLE IF NOT EXISTS ingredientes (
    id_ingrediente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_ingrediente TEXT NOT NULL,
    cantidad_medida TEXT
);

CREATE TABLE IF NOT EXISTS valoraciones (
    id_valoracion INTEGER PRIMARY KEY AUTOINCREMENT,
    puntaje INTEGER,
    comentario TEXT,
    fecha TEXT,
    id_receta INTEGER,
    id_usuario INTEGER,
    FOREIGN KEY (id_receta) REFERENCES recetas(id_receta),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);