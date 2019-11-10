class ComunidadesUsuario():
    def __init__(self, nombre, direccion, fecha_creacion, usuario):
        self.nombre         = nombre
        self.direccion      = direccion
        self.fecha_creacion = fecha_creacion
        self.usuario        = usuario

    def _lista_comunidades(self, usuario):
        # -- Va a la tabla COMUNIDADES y obtiene
        # -- las comunidades para ese usuario
        print(" has elegido lista de comunidades")

    def _crear_comunidad(self):
        print(" has elegido crear una comunidad")

    def _borrar_comunidad(self):
        print(" has elegido borrar esa comunidad")

    def opciones_comunidad(self, usuario):
        opcion_comunidad = int(input(" Elige una opcion para la COMUNIDAD: > "))
        if opcion_comunidad == 1:
            self._lista_comunidades(usuario)
        elif opcion_comunidad == 2:
            self._crear_comunidad()
        elif opcion_comunidad == 3:
            self._borrar_comunidad()
        elif opcion_comunidad == 4: # volver al menú anterior
            print(" has elegido volver al menú anterior")
            return


# ----

#senderistas = ComunidadesUsuario('senderistas', 'la montaña', '01/01/1998', 'gonza')

#senderistas.opciones_comunidad('gonza')
#print(senderistas.opciones_comunidad('gonza'))



