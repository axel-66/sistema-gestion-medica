from modelos.usuario import Usuario


class Medico(Usuario):

    def __init__(self, id, nombre, correo, contrasena,
                 especialidad, codigoProfesional):

        super().__init__(id, nombre, correo, contrasena)

        self.__especialidad = especialidad
        self.__codigoProfesional = codigoProfesional

    def consultarAgenda(self, citas):
        return [
            cita for cita in citas
            if cita.medico == self
        ]

    def atenderCita(self, cita):
        cita.cambiarEstado("Atendida")
        return "Cita atendida correctamente."

    @property
    def especialidad(self):
        return self.__especialidad

    @property
    def codigoProfesional(self):
        return self.__codigoProfesional