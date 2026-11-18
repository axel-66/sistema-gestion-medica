class CitaMedica:

    def __init__(self, idCita, fecha, especialidad, estado,
                 paciente, medico):

        self.__idCita = idCita
        self.__fecha = fecha
        self.__especialidad = especialidad
        self.__estado = estado

        # Relaciones de asociación del diagrama UML
        self.__paciente = paciente
        self.__medico = medico

    def programar(self):
        if not self.__especialidad.strip():
            raise ValueError("La especialidad es obligatoria.")

        self.__estado = "Programada"
        return "Cita programada correctamente."

    def cancelar(self):
        self.__estado = "Cancelada"

    def cambiarEstado(self, nuevoEstado):
        if not nuevoEstado.strip():
            raise ValueError("El estado no puede estar vacío.")

        self.__estado = nuevoEstado

    @property
    def idCita(self):
        return self.__idCita

    @property
    def fecha(self):
        return self.__fecha

    @property
    def especialidad(self):
        return self.__especialidad

    @property
    def estado(self):
        return self.__estado

    @property
    def paciente(self):
        return self.__paciente

    @property
    def medico(self):
        return self.__medico