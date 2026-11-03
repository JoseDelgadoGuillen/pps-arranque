# PPS-E1 · Lectura entrada→sink

Cópiala como `PPS-E1-lectura.md` y rellénala.

| Fichero | Punto de entrada | Sink(s) | Validación (¿cuál? ¿basta?) | Dónde falla según su modelo de ejecución |
|---|---|---|---|---|
| `validar.py` (interpretado) | sys.argv[1], argumento recibido por consola | con.execute(consulta), os.system() y eval(regla) | Comprueba que el nombre tenga entre 1 y 32 caracteres. No basta: permite caracteres especiales que pueden alterar consultas SQL, comandos del sistema o código ejecutado mediante eval() | El código fuente puede inspeccionarse. Además, eval() ejecuta cadenas como código Python, lo que puede provocar ejecución de código no deseado. También existe riesgo de inyección SQL y de comandos del sistema |
| `Validar.java` (bytecode / JVM) | args[0], argumento recibido por consola | st.executeQuery(consulta) y System.out.println() | Comprueba que el nombre no sea nulo, que tenga más de 0 caracteres y un máximo de 32. No basta: permite caracteres que pueden alterar la consulta SQL | La consulta SQL es vulnerable a inyección porque concatena directamente la entrada. Además, el bytecode puede descompilarse y permite descubrir la API Key incluida en el código |
| `validar.c` (nativo) | arg[1, argumento recibido por consola] | strcpy(buffer, nombre) y printf()| No existe validación de longitud. No basta: se pueden copiar más de 31 caracteres al buffer de 32 bytes, sin contar el terminador nulo | Desbordamiento de búfer (buffer overflow) en memoria de pila. Al superar los límites del array se produce comportamiento indefinido y puede corromperse memoria |

## ¿Cómo lo corregirías? (una línea por fichero)

- `validar.py`:Validar el formato de entrada, utilizar consultas SQL parametrizadas, evitar os.system() con datos externos y sustituir eval() por una operación segura.
- `Validar.java`:Utilizar PreparedStatement para las consultas SQL y almacenar las claves secretas fuera del código fuente.
- `validar.c`:Sustituir strcpy() por una copia con límites, comprobar la longitud y garantizar la terminación nula
