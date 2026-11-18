from datetime import datetime

from modelos.paciente import Paciente
from modelos.historia_clinica import HistoriaClinica
from modelos.medico import Medico
from modelos.cita_medica import CitaMedica

from servicios.sistema_gestion_medica import SistemaGestionMedica


def main():

    sistema = SistemaGestionMedica.obtenerInstancia()

    # Crear paciente
    paciente = Paciente(
        1,
        "Juan Pérez",
        "12345678",
        "987654321"
    )

    paciente.registrarDatos()

    # Crear historia clínica
    historia = HistoriaClinica(
        1,
        "Sin antecedentes registrados",
        "Primera consulta"
    )

    paciente.asignarHistoriaClinica(historia)

    # Registrar paciente
    sistema.registrarPaciente(paciente)

    # Crear médico
    medico = Medico(
        1,
        "Carlos Ramírez",
        "medico@essalud.com",
        "ClaveMedico123",
        "Medicina General",
        "CMP001"
    )

    # Crear cita médica
    cita = CitaMedica(
        1,
        datetime(2026, 12, 10, 9, 0),
        "Medicina General",
        "Pendiente",
        paciente,
        medico
    )

    sistema.agregarCita(cita)

    # Mostrar resultados
    print("SISTEMA DE GESTIÓN MÉDICA")
    print("-------------------------")
    print("Paciente:", paciente.nombre)
    print("Citas registradas:", len(sistema.citas))

    print("\nREPORTE DE PACIENTES")
    print(sistema.generarReporte("pacientes"))

    print("\nREPORTE DE CITAS")
    print(sistema.generarReporte("citas"))


if __name__ == "__main__":
    main()