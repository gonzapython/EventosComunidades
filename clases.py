class Usuarios():
    def __init__(self, nombre, contrasena, es_creador, es_organizador):
        self.nombre         = nombre
        self.contrasena     = contrasena
        self.es_creador     = es_creador
        self.es_organizador = es_organizador
#
usuario = Usuarios(self.nombre, self.contrasena)

class Comunidades():
    def __init__(self, nombre, direccion, fecha_creacion, creador, organizador):
        self.nombre         = nombre
        self.direccion      = direccion
        self.fecha_creacion = fecha_creacion
        self.creador        = creador
        self.organizador    = organizador
#
comunidad = Comunidades(self.nombre, self.direccion, self.fecha_creacion, self.creador, self.organizador)

class Eventos():
    def __init__(self, nombre, descripcion, fecha):
        self.nombre      = nombre
        self.descripcion = descripcion
        self.fecha       = fecha
#
evento = Eventos(self.nombre, self.descripcion, self.fecha)
