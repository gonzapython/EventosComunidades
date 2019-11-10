class EventosUsuarioComunidad():
    def __init__(self, nombre, descripcion, fecha, usuario, comunidad):
        self.nombre      = nombre
        self.descripcion = descripcion
        self.fecha       = fecha
        self.usuario     = usuario
        self.comunidad   = comunidad


    def _lista_eventos(self, usuario, comunidad):
        # -- Accede a la tabla de EVENTOS y obtiene
        # -- los eventos para ese usuario y comunidad
        print(" has elegido lista de eventos")

    def _lista_eventos_asiste(self, usuario, comunidad):
        # -- Accede a la tabla de EVENTOS y obtiene
        # -- los eventos a los q ya se ha apuntado ese usuario (y comunidad)
        print(" has elegido lista de eventos q quieres asistir")

    def _detalles_evento(self):
        # -- Accede a la tabla de EVENTOS y obtiene
        # -- toda la información de ese evento
        print(" has elegido detalle de evento")

    def _modificar_evento(self):
        print(" has elegido modificar evento")

    def _crear_evento(self):
        print(" has elegido crear evento")

    def _borrar_evento(self):
        print(" has elegido borrar evento")


    def opciones_evento(self, usuario, comunidad):
        opcion_evento = int(input(" Elige una opcion para el EVENTO: > "))
        if opcion_evento == 1:
            self._lista_eventos_asiste(usuario, comunidad)
        elif opcion_evento == 2:
            self._lista_eventos(usuario, comunidad)
        elif opcion_evento == 3:
            self._crear_evento()
        elif opcion_evento == 4:
            self._modificar_evento()
        elif opcion_evento == 5:
            self._borrar_evento()
        elif opcion_evento == 6:  # volver al menú anterior
            print(" has elegido volver al menú anterior")
            return


# ----

#veramanecer = EventosUsuarioComunidad('amaneciendo', 'ir a ver amanecer', '01/02/2021', 'gonza', 'senderistas')

#veramanecer.opciones_evento('gonza', 'senderistas')







