from reportes.reporte import Reporte


class ReporteCitas(Reporte):

    def __init__(self, citas):
        super().__init__()
        self.__citas = citas

    def generar(self):
        return list(map(
            lambda cita: {
                "idCita": cita.idCita,
                "fecha": str(cita.fecha),
                "especialidad": cita.especialidad,
                "estado": cita.estado
            },
            self.__citas
        ))