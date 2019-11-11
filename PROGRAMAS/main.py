from usuario   import Usuarios
from comunidad import ComunidadesUsuario
from evento    import EventosUsuarioComunidad

#usuario   = Usuarios()
#evento    = EventosUsuarioComunidad(usuario, comunidad)
#comunidad = ComunidadesUsuario(usuario, evento)

nombre = 'jose'

usuario   = Usuarios('jose','aaaaaa', 'c', 'o')
evento    = EventosUsuarioComunidad('hackeando cañas',
                                    'lalalala', 'fecha',
                                     usuario, comunidad)
comunidad = ComunidadesUsuario('OSW','calle de la luz','10/10/10',  usuario, evento)



def main():
    usuario.login()
    

# -----
main()

