-- Tabla de USUARIOS
-- =================
CREATE TABLE usuarios (
    usuario_id  INTEGER PRIMARY KEY,
    nombre      varchar NOT NULL,
    contraseña  varchar NOT NULL,
    ind_creador_organizador varchar NOT NULL, -- 'C', 'O', 'N'
);

-- Tabla de COMUNIDADES
-- ====================
CREATE TABLE comunidades (
    comunidad_id    INTEGER PRIMARY KEY,
    nombre          varchar NOT NULL,
    direc_social    varchar NOT NULL,
    fecha_creacion  date NOT NULL,
    creador_id      INTEGER NOT NULL,
    organizador_id  INTEGER NOT NULL,
    FOREIGN KEY creador_usuario (creador_id)
      REFERENCES usuarios (user_id),
    FOREIGN KEY organizador_usuario (organizador_id)
      REFERENCES usuarios (user_id)
);

-- Tabla de EVENTOS
-- ================
CREATE TABLE eventos (
    evento_id     INTEGER PRIMARY KEY,
    nombre        varchar NOT NULL,
    descripcion   varchar NOT NULL,
    fecha         date NOT NULL
);

