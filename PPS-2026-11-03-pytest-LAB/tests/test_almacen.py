from inscripciones.almacen import guardar_inscripcion, leer_inscripciones


def test_guardar_y_leer(tmp_path):
    ruta = tmp_path / "inscripciones.csv"
    datos = {"dni": "12345678Z", "nombre": "Ana García", "email": "ana@ejemplo.es",
             "edad": 30, "cuota": 60.0}
    guardar_inscripcion(ruta, datos)
    filas = leer_inscripciones(ruta)
    assert len(filas) == 1
    assert filas[0]["nombre"] == "Ana García"
