"""Validación de los datos de una inscripción.

Las reglas que debe cumplir este módulo están en ESPECIFICACION.md.
"""
import re

LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"


def validar_dni(dni: str) -> bool:
    """Devuelve True si el DNI tiene formato válido y la letra es correcta."""
    dni = dni.strip()
    if not re.fullmatch(r"\d+[A-Za-z]", dni):
        return False
    numero, letra = int(dni[:-1]), dni[-1]
    return letra == LETRAS_DNI[numero % 23]


def validar_email(email: str) -> bool:
    """Comprobación sencilla: algo@algo.dominio, sin espacios."""
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", email.strip()) is not None


def normalizar_nombre(nombre: str) -> str:
    """Quita espacios sobrantes y pone mayúscula inicial en cada palabra."""
    partes = nombre.split()
    if not partes:
        raise ValueError("el nombre no puede estar vacío")
    return " ".join(p.capitalize() for p in partes)


def calcular_cuota(edad: int, desempleado: bool = False) -> float:
    """Cuota mensual en euros según la edad y la situación laboral."""
    if edad < 16:
        raise ValueError("la edad mínima es 16 años")
    cuota = 40.0 if edad < 25 else 60.0
    if desempleado:
        cuota = cuota / 2
    return cuota
