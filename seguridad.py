import bcrypt
import maskpass


def solicitar_contrasena(prompt: str = "Contraseña: ") -> str:
    return maskpass.askpass(prompt=prompt, mask="*")


def hashear_contrasena(contrasena_plana: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(contrasena_plana.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verificar_contrasena(contrasena_plana: str, hash_guardado: str) -> bool:
    if not contrasena_plana or not hash_guardado:
        return False
    try:
        return bcrypt.checkpw(
            contrasena_plana.encode("utf-8"),
            hash_guardado.encode("utf-8"),
        )
    except ValueError:
        return False