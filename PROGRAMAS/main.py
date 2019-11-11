from usuario   import Usuarios
from comunidad import ComunidadesUsuario
from evento    import EventosUsuarioComunidad

#usuario   = Usuarios()
#evento    = EventosUsuarioComunidad(usuario, comunidad)
#comunidad = ComunidadesUsuario(usuario, evento)

usuario   = Usuarios()
comunidad = ComunidadesUsuario(usuario)
evento    = EventosUsuarioComunidad(comunidad)

def main():
    login()

# -----
main()

