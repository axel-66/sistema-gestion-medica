
from abc import ABC
from seguridad.proteccion_datos import generar_hash, verificar_contrasena


class Usuario(ABC):

    def __init__(self, id, nombre, correo, contrasena):
        self.__id = id
        self.__nombre = nombre
        self.__correo = correo
        self.__contrasenaHash = generar_hash(contrasena)

    def iniciarSesion(self, contrasena):
        return verificar_contrasena(
            contrasena,
            self.__contrasenaHash
        )

    def cerrarSesion(self):
        return "Sesión cerrada correctamente."

    def actualizarDatos(self, nombre=None, correo=None):
        if nombre is not None and nombre.strip():
            self.__nombre = nombre

        if correo is not None and correo.strip():
            self.__correo = correo

        return "Datos del usuario actualizados correctamente."

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def contrasenaHash(self):
        return self.__contrasenaHash
