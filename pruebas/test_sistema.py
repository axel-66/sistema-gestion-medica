
import unittest
from datetime import datetime

from modelos.usuario import Usuario
from modelos.paciente import Paciente
from modelos.medico import Medico
from modelos.cita_medica import CitaMedica
from servicios.sistema_gestion_medica import SistemaGestionMedica


class UsuarioPrueba(Usuario):
    pass


class TestSistemaGestionMedica(unittest.TestCase):

    def setUp(self):
        # Reiniciar los datos del Singleton para cada prueba
        sistema = SistemaGestionMedica.obtenerInstancia()
        sistema._SistemaGestionMedica__pacientes.clear()
        sistema._SistemaGestionMedica__citas.clear()
        self.sistema = sistema

        self.paciente = Paciente(
            1, "Juan Pérez", "12345678", "987654321"
        )

        self.medico = Medico(
            1, "Carlos Ramírez", "medico@essalud.com",
            "ClaveMedico123", "Medicina General", "CMP001"
        )

    def test_registrar_paciente(self):
        self.sistema.registrarPaciente(self.paciente)

        self.assertEqual(len(self.sistema.pacientes), 1)
        self.assertEqual(
            self.sistema.pacientes[0].nombre, "Juan Pérez"
        )

    def test_registrar_cita(self):
        self.sistema.registrarPaciente(self.paciente)

        cita = CitaMedica(
            1, datetime(2026, 12, 10, 9, 0),
            "Medicina General", "Pendiente",
            self.paciente, self.medico
        )

        self.sistema.agregarCita(cita)

        self.assertEqual(len(self.sistema.citas), 1)
        self.assertEqual(cita.estado, "Programada")
        self.assertEqual(
            len(self.paciente.consultarCitas()), 1
        )

    def test_generar_reporte_pacientes(self):
        self.sistema.registrarPaciente(self.paciente)

        reporte = self.sistema.generarReporte("pacientes")

        self.assertEqual(len(reporte), 1)
        self.assertEqual(reporte[0]["nombre"], "Juan Pérez")

    def test_verificar_contrasena_correcta(self):
        usuario = UsuarioPrueba(
            1, "Axel", "axel@essalud.com", "ClaveSegura123"
        )

        self.assertTrue(
            usuario.iniciarSesion("ClaveSegura123")
        )

    def test_rechazar_contrasena_incorrecta(self):
        usuario = UsuarioPrueba(
            2, "Carlos", "carlos@essalud.com", "ClaveSegura123"
        )

        self.assertFalse(
            usuario.iniciarSesion("ClaveIncorrecta")
        )


if __name__ == "__main__":
    unittest.main()
