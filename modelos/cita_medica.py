
from datetime import datetime
from modelos.paciente import Paciente
from modelos.medico import Medico


class CitaMedica:

    def __init__(self, idCita, fecha, especialidad, estado,
                 paciente, medico):

        if not isinstance(paciente, Paciente):
            raise TypeError("Debe asignarse un paciente válido.")

        if not isinstance(medico, Medico):
            raise TypeError("Debe asignarse un médico válido.")

        if not isinstance(fecha, datetime):
            raise TypeError("La fecha debe ser un objeto datetime.")

        self.__idCita = idCita
        self.__fecha = fecha
        self.__especialidad = especialidad
        self.__estado = estado
        self.__paciente = paciente
        self.__medico = medico

    def programar(self):
        if not self.__especialidad.strip():
            raise ValueError("La especialidad es obligatoria.")

        self.__estado = "Programada"
        return "Cita programada correctamente."

    def cancelar(self):
        self.__estado = "Cancelada"
        return "Cita cancelada correctamente."

    def cambiarEstado(self, nuevoEstado):
        estados_validos = [
            "Pendiente",
            "Programada",
            "Cancelada",
            "Atendida"
        ]

        if nuevoEstado not in estados_validos:
            raise ValueError("El estado de la cita no es válido.")

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
