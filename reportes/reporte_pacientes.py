from reportes.reporte import Reporte


class ReportePacientes(Reporte):

    def __init__(self, pacientes):
        super().__init__()
        self.__pacientes = pacientes

    def generar(self):
        return list(map(
            lambda paciente: {
                "idPaciente": paciente.idPaciente,
                "nombre": paciente.nombre
            },
            self.__pacientes
        ))