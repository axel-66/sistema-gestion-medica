
from modelos.usuario import Usuario


class Administrador(Usuario):

    def crearUsuario(self, usuario, usuarios):
        if not isinstance(usuario, Usuario):
            raise TypeError("El objeto debe ser un usuario.")

        usuarios.append(usuario)
        return "Usuario creado correctamente."

    def modificarUsuario(self, usuario, nombre=None, correo=None):
        if not isinstance(usuario, Usuario):
            raise TypeError("El objeto debe ser un usuario.")

        return usuario.actualizarDatos(nombre, correo)

    def supervisarSistema(self, sistema):
        return {
            "totalPacientes": len(sistema.pacientes),
            "totalCitas": len(sistema.citas)
        }
