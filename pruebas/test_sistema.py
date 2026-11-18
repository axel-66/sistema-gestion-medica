
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

    def crear_cita(self, id_cita=1, especialidad="Medicina General"):
        return CitaMedica(
            id_cita,
            datetime(2026, 12, 10, 9, 0),
            especialidad,
            "Pendiente",
            self.paciente,
            self.medico
        )

    # PRUEBAS DE FUNCIONAMIENTO

    def test_registrar_paciente(self):
        self.sistema.registrarPaciente(self.paciente)

        self.assertEqual(len(self.sistema.pacientes), 1)
        self.assertEqual(
            self.sistema.pacientes[0].nombre, "Juan Pérez"
        )

    def test_registrar_cita(self):
        self.sistema.registrarPaciente(self.paciente)
        cita = self.crear_cita()

        self.sistema.agregarCita(cita)

        self.assertEqual(len(self.sistema.citas), 1)
        self.assertEqual(cita.estado, "Programada")
        self.assertEqual(len(self.paciente.consultarCitas()), 1)

    def test_generar_reporte_pacientes(self):
        self.sistema.registrarPaciente(self.paciente)

        reporte = self.sistema.generarReporte("pacientes")

        self.assertEqual(len(reporte), 1)
        self.assertEqual(reporte[0]["nombre"], "Juan Pérez")

    # PRUEBAS DE AUTENTICACIÓN

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

    # PRUEBAS DE VALIDACIÓN

    def test_rechazar_paciente_con_dni_invalido(self):
        paciente = Paciente(
            2, "Pedro López", "1234", "987654321"
        )

        with self.assertRaises(ValueError):
            self.sistema.registrarPaciente(paciente)

    def test_rechazar_paciente_duplicado(self):
        self.sistema.registrarPaciente(self.paciente)

        paciente_duplicado = Paciente(
            1, "Pedro López", "87654321", "999888777"
        )

        with self.assertRaises(ValueError):
            self.sistema.registrarPaciente(paciente_duplicado)

    def test_rechazar_cita_sin_especialidad(self):
        self.sistema.registrarPaciente(self.paciente)
        cita = self.crear_cita(especialidad="")

        with self.assertRaises(ValueError):
            self.sistema.agregarCita(cita)

    def test_rechazar_cita_duplicada(self):
        self.sistema.registrarPaciente(self.paciente)

        cita1 = self.crear_cita(1)
        cita2 = self.crear_cita(1)

        self.sistema.agregarCita(cita1)

        with self.assertRaises(ValueError):
            self.sistema.agregarCita(cita2)

    def test_rechazar_estado_invalido(self):
        cita = self.crear_cita()

        with self.assertRaises(ValueError):
            cita.cambiarEstado("Estado incorrecto")

    def test_rechazar_cita_de_paciente_no_registrado(self):
        cita = self.crear_cita()

        with self.assertRaises(ValueError):
            self.sistema.agregarCita(cita)


if __name__ == "__main__":
    unittest.main()
