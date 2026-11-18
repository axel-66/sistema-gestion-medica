
from modelos.paciente import Paciente
from modelos.cita_medica import CitaMedica
from reportes.fabrica_reportes import FabricaReportes


class SistemaGestionMedica:

    __instancia = None

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

    def __init__(self):
        if not hasattr(self, "_inicializado"):
            self.__pacientes = []
            self.__citas = []
            self._inicializado = True

    @classmethod
    def obtenerInstancia(cls):
        return cls()

    def registrarPaciente(self, paciente):
        if not isinstance(paciente, Paciente):
            raise TypeError("El objeto debe ser un paciente.")

        if any(
            p.idPaciente == paciente.idPaciente
            for p in self.__pacientes
        ):
            raise ValueError("El paciente ya está registrado.")

        paciente.registrarDatos()
        self.__pacientes.append(paciente)

    def agregarCita(self, cita):
        if not isinstance(cita, CitaMedica):
            raise TypeError("El objeto debe ser una cita médica.")

        if any(
            c.idCita == cita.idCita
            for c in self.__citas
        ):
            raise ValueError("La cita ya está registrada.")

        if not any(
            p.idPaciente == cita.paciente.idPaciente
            for p in self.__pacientes
        ):
            raise ValueError(
                "El paciente no está registrado en el sistema."
            )

        cita.programar()
        self.__citas.append(cita)
        cita.paciente.agregarCita(cita)

    def generarReporte(self, tipo):
        fabrica = FabricaReportes()
        reporte = fabrica.crearReporte(
            tipo,
            self.__pacientes,
            self.__citas
        )
        return reporte.generar()

    def buscarPacientes(self, nombre):
        return list(filter(
            lambda paciente: nombre.lower() in paciente.nombre.lower(),
            self.__pacientes
        ))

    @property
    def pacientes(self):
        return self.__pacientes.copy()

    @property
    def citas(self):
        return self.__citas.copy()
