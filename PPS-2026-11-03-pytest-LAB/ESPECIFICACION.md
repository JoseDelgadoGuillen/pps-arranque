# Especificación del módulo de inscripciones

El club de robótica guarda las inscripciones en un CSV que luego abre la secretaría
con una hoja de cálculo. Estas son las reglas. El código tiene que cumplirlas todas.

## R1. DNI

- Exactamente 8 cifras seguidas de una letra.
- La letra es la que corresponde a `número % 23` en la tabla `TRWAGMYFPDXBNJZSQVHLCKE`.
- Se acepta la letra en minúscula (`12345678z` es válido).
- Se ignoran los espacios al principio y al final.

## R2. Correo electrónico

- Formato `usuario@dominio.ext`, sin espacios, con una sola `@`.

## R3. Nombre

- Se quitan los espacios sobrantes y cada palabra empieza por mayúscula.
- Un nombre vacío o solo con espacios lanza `ValueError`.

## R4. Cuota mensual

| Edad | Cuota |
|---|---|
| Menos de 16 | No se admite: lanza `ValueError` |
| De 16 a 25 (ambos incluidos) | 40 € |
| Más de 25 | 60 € |

Las personas desempleadas pagan la mitad.

## R5. Almacenamiento seguro

- Ningún campo guardado en el CSV puede empezar por `=`, `+`, `-`, `@`, tabulador o
  retorno de carro sin neutralizar. Para neutralizarlo se le antepone una comilla simple `'`.
- Motivo: si alguien se inscribe con el nombre `=HYPERLINK("http://...")`, la hoja de
  cálculo de la secretaría lo ejecutaría como fórmula (inyección de fórmulas en CSV).
