from inscripciones.validacion import validar_dni, validar_email, calcular_cuota


def test_dni_valido():
    assert validar_dni("12345678Z")


def test_dni_letra_incorrecta():
    assert not validar_dni("12345678A")


def test_email_valido():
    assert validar_email("ana.garcia@ejemplo.es")


def test_cuota_adulto():
    assert calcular_cuota(40) == 60.0
