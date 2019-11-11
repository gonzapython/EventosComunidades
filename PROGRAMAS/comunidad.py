class ComunidadesUsuario():
    def __init__(self, nombre, direccion, fecha_creacion, usuario, evento):
        self.nombre         = nombre
        self.direccion      = direccion
        self.fecha_creacion = fecha_creacion
        self.usuario        = usuario
        self.evento         = evento


    def _lista_comunidades(self, usuario):
        # -- Va a la tabla COMUNIDADES y obtiene
        # -- las comunidades para ese usuario
        print(" has elegido lista de comunidades")

    def _crear_comunidad(self):
        print(" has elegido crear una comunidad")

    def _borrar_comunidad(self):
        print(" has elegido borrar esa comunidad")

    def opciones_comunidad(self, usuario):
        # ir a la tabla COMUNIDAD_EVENTOS_USUARIO y sacar los EVENTOS (con sus datos) 
        # de ese usuario/comunidad.
        # Para cada una de ellas, hacer:
        nombre_evento_BD      = 'subir a peñalara'
        descripcion_evento_BD = 'escalada nivel 1'
        fecha_evento_BD       = '01/04/2021'
        #
        self.evento.opciones_evento(usuario, self.nombre)


# ----

#senderistas = ComunidadesUsuario('senderistas', 'la montaña', '01/01/1998', 'gonza')

#senderistas.opciones_comunidad('gonza')
#print(senderistas.opciones_comunidad('gonza'))



