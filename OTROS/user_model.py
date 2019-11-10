class Usuarios():
    def __init__(self, nombre, contrasena):
        self.nombre         = nombre
        self.contrasena     = contrasena
#
usuario = Usuarios(self.nombre, self.contrasena)

def _ver_creador_organizador():
    # accede a la tabla de USUARIOS y obtiene esa información
    pass:

def _menu_creador_organizador():
    # mostrar el menú de usuario creador/organizador
    pass:

def _menu_usuario_normal():
    # mostrar el menú de usuario normal
    pass:

def _ver_menu(self, usuario.nombre):
    tipo_usuario = self._ver_creador_organizador()
    if tipo_usuario == 'C' or  tipo_usuario == 'O':
        self._menu_creador_organizador()
    elif tipo_usuario == 'N':
        self._menu_usuario_normal()








class Comunidades():
    def __init__(self, nombre, direccion, fecha_creacion, creador, organizador):
        self.nombre         = nombre
        self.direccion      = direccion
        self.fecha_creacion = fecha_creacion
        self.creador        = creador
        self.organizador    = organizador
#
comunidad = Comunidades(self.nombre, self.direccion, self.fecha_creacion, self.creador, self.organizador)

def _lista_comunidades(usuario.nombre):
    pass:

def _crear_comunidad():

def _borrar_comunidad():






class Eventos():
    def __init__(self, nombre, descripcion, fecha):
        self.nombre      = nombre
        self.descripcion = descripcion
        self.fecha       = fecha
#
evento = Eventos(self.nombre, self.descripcion, self.fecha)


def _lista_eventos(usuario.nombre, usuario.comunidad):

def _lista_eventos_asiste(usuario.nombre, usuario.comunidad):

def _ver_evento(evento.nombre):

def _modificar_evento(evento.nombre):

def _crear_evento():





# -------------------------------


# -- LOGIN --------------------------------------
    def login(self):
        print(" Escribe tu usuario y tu contraseña ")
        usuario = input(" Usuario: ")
        contraseña = input(" Contraseña: ")
        self._validar_usuario_login(usuario, contraseña)

        self._ver_menu(usuario, contraseña)

        



