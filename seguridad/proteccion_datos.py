import hashlib


def generar_hash(contrasena):
    """Genera el hash de una contraseña."""
    return hashlib.sha256(contrasena.encode("utf-8")).hexdigest()


def verificar_contrasena(contrasena, contrasena_hash):
    """Verifica si la contraseña coincide con su hash."""
    return generar_hash(contrasena) == contrasena_hash