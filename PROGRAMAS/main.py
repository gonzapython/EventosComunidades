from usuario   import Usuarios
from comunidad import ComunidadesUsuario
from precomunidad import Comunidades
from evento    import EventosUsuarioComunidad

#usuario   = Usuarios()
#evento    = EventosUsuarioComunidad(usuario, comunidad)
#comunidad = ComunidadesUsuario(usuario, evento)

nombre = 'jose'

usuario   = Usuarios('jose','aaaaaa', 'c', 'o', 'comunidad2')
evento    = EventosUsuarioComunidad('hackeando cañas',
                                    'lalalala', 'fecha',
                                     usuario)
#comunidad = ComunidadesUsuario('OSW','calle de la luz','10/10/10', usuario, evento)

comunidad = Comunidades('OSW','calle de la luz','10/10/10')

# -- para que 'comunidad' sea un objeto (no un str) y
# -- pueda usarlo para enlazar el usuario con la comunidad
# -- de usuario.py a comunidad.py : self.comunidadusuario.opciones_comunidad(self.nombre)
# --
comunidadusuario = ComunidadesUsuario('OSW','calle de la luz','10/10/10', usuario, comunidad, evento)
# --


def main():
    usuario.login()


# -----
main()

