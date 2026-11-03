"""Guarda y lee las inscripciones en un fichero CSV."""
import csv
from pathlib import Path

CAMPOS = ["dni", "nombre", "email", "edad", "cuota"]


def neutralizar(valor: str) -> str:
    """Evita que una hoja de cálculo interprete el texto como una fórmula."""
    if valor.startswith("="):
        return "'" + valor
    return valor


def guardar_inscripcion(ruta: Path, datos: dict) -> None:
    """Añade una fila al CSV. Si el fichero no existe, escribe antes la cabecera."""
    ruta = Path(ruta)
    nuevo = not ruta.exists()
    with ruta.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        w.writerow({c: neutralizar(str(datos[c])) for c in CAMPOS})


def leer_inscripciones(ruta: Path) -> list[dict]:
    with Path(ruta).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
