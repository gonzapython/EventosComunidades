class Usuarios():
    def __init__(self, nombre, contrasena, creador, organizador):
        self.nombre      = nombre
        self.contrasena  = contrasena
        self.creador     = creador
        self.organizador = organizador


def _validar_usuario_tipo(self, usuario, contrasena):
    # accede a la tabla de USUARIOS y:
    #  - comprueba login y password
    #     - si no son correctos:
    #           - volver a intentar
    #     - si son correctos:
    #           - retorna el tipo: obtiene si es 'C' (creador), 'O' (organizador), ó 'N' (normal)
    pass

def _menu_creador_organizador(self, usuario.nombre):
    # mostrar el menú de usuario creador/organizador
    pass

def _menu_usuario_normal(self, usuario.nombre):
    # mostrar el menú de usuario normal

    opcion = int(input(" Elige una opcion: > "))

    if opcion == 1:
        return opcion


def _ver_menu(self, usuario, tipo_usuario):
    if tipo_usuario == 'C' or  tipo_usuario == 'O':
        self._menu_creador_organizador(usuario)
    elif tipo_usuario == 'N':
        opcion = self._menu_usuario_normal(usuario)


# -- LOGIN -----
def login(self):
    print(" Escribe tu usuario y tu contraseña ")
    usuario = input(" Usuario: ")
    contrasena = input(" Contraseña: ")
    tipo_usuario = self._validar_usuario_login(usuario, contrasena)
    opcion = self._ver_menu(usuario, contrasena, tipo_usuario)


# -- REGISTRARSE ----
def registrarse(self):
    pass


