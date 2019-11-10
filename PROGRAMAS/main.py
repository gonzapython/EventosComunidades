from usuario   import Usuarios
from comunidad import ComunidadesUsuario
from evento    import EventosUsuarioComunidad

usuario   = Usuarios(comunidad)
evento    = EventosUsuarioComunidad(usuario, comunidad)
comunidad = ComunidadesUsuario(usuario, evento)

def main():
    usuario.login()

    opciones_comunidad(opcion, usuario)

# -----
main()

