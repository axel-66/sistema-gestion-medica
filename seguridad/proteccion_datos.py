
import hashlib
import secrets
import hmac


def generar_hash(contrasena):
    """Genera un hash seguro de la contraseña con salt aleatorio."""

    salt = secrets.token_bytes(16)

    hash_bytes = hashlib.pbkdf2_hmac(
        "sha256",
        contrasena.encode("utf-8"),
        salt,
        600000
    )

    return salt.hex() + ":" + hash_bytes.hex()


def verificar_contrasena(contrasena, contrasena_hash):
    """Verifica una contraseña utilizando su salt original."""

    try:
        salt_hex, hash_original = contrasena_hash.split(":")
        salt = bytes.fromhex(salt_hex)

        hash_nuevo = hashlib.pbkdf2_hmac(
            "sha256",
            contrasena.encode("utf-8"),
            salt,
            600000
        ).hex()

        return hmac.compare_digest(hash_nuevo, hash_original)

    except (ValueError, TypeError):
        return False
