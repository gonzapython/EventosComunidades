from comunidad import ComunidadesUsuario

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

    def _menu_creador_organizador(self, usuario):
        # mostrar el menú de usuario creador/organizador
        # ir a la tabla USUARIOS_COMUNIDAD y sacar las comunidades (con sus datos) de ese usuario
        # para cada una de ellas, hacer:
        nombre_comunid_BD       = 'senderistas'
        direcc_comunid_BD       = 'la montaña'
        fecha_creacc_comunid_BD = '01/11/1998'
        #
        comunidad = ComunidadesUsuario(nombre_comunid_BD, direcc_comunid_BD, fecha_creacc_comunid_BD, usuario)
        comunidad.opciones_comunidad(usuario)

    def _menu_usuario_normal(self, usuario):
        # mostrar el menú de usuario normal
        # ir a la tabla USUARIOS_COMUNIDAD y sacar las comunidades de ese usuario
        # para cada una de ellas, hacer:
        nombre_comunid_BD       = 'senderistas'
        direcc_comunid_BD       = 'la montaña'
        fecha_creacc_comunid_BD = '01/11/1998'
        #
        comunidad = ComunidadesUsuario(nombre_comunid_BD, direcc_comunid_BD, fecha_creacc_comunid_BD, usuario)
        comunidad.opciones_comunidad(usuario)

    def _ver_menu(self, usuario, tipo_usuario):
        # -- pongo tipo_usuario
        tipo_usuario = 'N'
        if tipo_usuario == 'C' or  tipo_usuario == 'O':
            opcion_usuario = self._menu_creador_organizador(usuario)
        elif tipo_usuario == 'N':
            opcion_usuario = self._menu_usuario_normal(usuario)
        return opcion_usuario

    # -- LOGIN -----
    def login(self):
        print(" Escribe tu usuario y tu contraseña ")
        usuario = input(" Usuario: ")
        contrasena = input(" Contraseña: ")
        tipo_usuario = self._validar_usuario_tipo(usuario, contrasena)
        opcion = self._ver_menu(usuario, tipo_usuario)
        return opcion, usuario

    # -- REGISTRARSE ----
    def registrarse(self):
        pass


# ----

#gonza = Usuarios('gonza', 'hhgg', 'S', 'N')

#opcion, usuario = gonza.login()
#print(f' opcion y usuario {opcion} y {usuario}')


