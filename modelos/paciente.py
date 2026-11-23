
from modelos.historia_clinica import HistoriaClinica


class Paciente:

    def __init__(self, idPaciente, nombre, dni, telefono):
        self.__idPaciente = idPaciente
        self.__nombre = nombre
        self.__dni = dni
        self.__telefono = telefono
        self.__historiaClinica = None
        self.__citas = []

    def registrarDatos(self):
        if not self.__nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if len(self.__dni) != 8 or not self.__dni.isdigit():
            raise ValueError("El DNI debe contener 8 dígitos.")

        return "Datos del paciente registrados correctamente."

    def actualizarDatos(self, nombre=None, telefono=None):
        if nombre is not None:
            if not nombre.strip():
                raise ValueError("El nombre no puede estar vacío.")
            self.__nombre = nombre

        if telefono is not None:
            if not telefono.strip():
                raise ValueError("El teléfono no puede estar vacío.")
            self.__telefono = telefono

        return "Datos actualizados correctamente."

    def consultarCitas(self):
        return self.__citas.copy()

    def agregarCita(self, cita):
        if cita in self.__citas:
            raise ValueError("La cita ya está asignada al paciente.")
        self.__citas.append(cita)

    def asignarHistoriaClinica(self, historia):
        if not isinstance(historia, HistoriaClinica):
            raise TypeError("Debe asignarse una historia clínica válida.")
        self.__historiaClinica = historia

    @property
    def idPaciente(self):
        return self.__idPaciente

    @property
    def nombre(self):
        return self.__nombre

    @property
    def dni(self):
        return self.__dni

    @property
    def telefono(self):
        return self.__telefono

    @property
    def historiaClinica(self):
        return self.__historiaClinica
