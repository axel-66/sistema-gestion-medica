from modelos.usuario import Usuario


class Administrador(Usuario):

    def crearUsuario(self, usuario, usuarios):
        usuarios.append(usuario)
        return "Usuario creado correctamente."

    def modificarUsuario(self, usuario, nombre=None, correo=None):
        if nombre:
            usuario._Usuario__nombre = nombre

        if correo:
            usuario._Usuario__correo = correo

        return "Usuario modificado correctamente."

    def supervisarSistema(self, sistema):
        return {
            "totalPacientes": len(sistema.pacientes),
            "totalCitas": len(sistema.citas)
        }