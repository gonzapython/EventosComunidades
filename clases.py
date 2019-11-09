
class Usuarios():
    def __init__(self, nombre, contrasena):
        self.nombre     = nombre
        self.contrasena = contrasena
#
usuario = Usuarios(self.nombre, self.contrasena)

class Comunidades():
    def __init__(self, nombre, direccion, fecha_creacion, creador, organizador):
        self.nombre = nombre
        self.direccion = direccion
        self.fecha_creacion = fecha_creacion
        self.creador = creador
        self.organizador = organizador
#
comunidad = Comunidades(self.nombre, self.direccion, self.fecha_creacion, self.creador, self.organizador)

class Eventos():
    def __init__(self, nombre, descripcion, fecha):
        self.nombre      = nombre
        self.descripcion = descripcion
        self.fecha       = fecha
#
evento = Eventos(self.nombre, self.descripcion, self.fecha)

class MiembrosComunidad():
    def __init__(self, nombre, comunidad):
        self.nombre    = usuario.nombre
        self.comunidad = comunidad.nombre
#
miembrocomunidad = MiembrosComunidad(self.nombre, self.comunidad)

class AsistentesEventos():
    def __init__(self, asistente, evento):
        self.asistente = usuario.nombre
        self.evento    = evento.nombre
#
asistenteevento = AsistentesEventos(self.evento, self.evento)
