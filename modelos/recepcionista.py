from modelos.usuario import Usuario


class Recepcionista(Usuario):

    def registrarPaciente(self, sistema, paciente):
        sistema.registrarPaciente(paciente)
        return "Paciente registrado correctamente."

    def programarCita(self, sistema, cita):
        sistema.agregarCita(cita)
        return "Cita programada correctamente."

    def cancelarCita(self, cita):
        cita.cancelar()
        return "Cita cancelada correctamente."