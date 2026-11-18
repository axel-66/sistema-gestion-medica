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
        if nombre:
            self.__nombre = nombre

        if telefono:
            self.__telefono = telefono

        return "Datos actualizados correctamente."

    def consultarCitas(self):
        return self.__citas.copy()

    def agregarCita(self, cita):
        self.__citas.append(cita)

    def asignarHistoriaClinica(self, historia):
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