from reportes.reporte_pacientes import ReportePacientes
from reportes.reporte_citas import ReporteCitas


class FabricaReportes:

    @staticmethod
    def crearReporte(tipo, pacientes, citas):

        if tipo == "pacientes":
            return ReportePacientes(pacientes)

        elif tipo == "citas":
            return ReporteCitas(citas)

        else:
            raise ValueError("Tipo de reporte no válido.")