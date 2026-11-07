# Tarea 2: Obteniendo información de un directorio

- Autor: Angel Escobar
- Materia: Sistemas Operativos
- Grupo: 7
- Profesor: DR. GUNNAR EYAL WOLF ISZAEVICH
- Facultad de Ingeniería, UNAM

Lo hice en Python 3 y sólo usa la biblioteca estándar (`os`, `sys` y `time`). Se corre así:

    python3 archivos_recientes.py <directorio> <días>

Por ejemplo, `python3 archivos_recientes.py /tmp 3` muestra lo que se modificó en `/tmp` en los últimos 3 días.

Primero reviso que vengan los dos parámetros, que los días sean un número y que el directorio exista; si algo falla imprime cómo se invoca y termina. Después saco el límite restando los días (en segundos) a la hora actual. Abro el directorio con `os.scandir()` y a cada entrada le pido su `stat()` sin seguir ligas simbólicas. Si su `st_mtime` es mayor o igual al límite la guardo en una lista junto con su nombre.

Al final ordeno la lista con `sorted()`, que la ordena por nombre, e imprimo el nombre, la fecha de modificación, el modo en octal y el tamaño en bytes, con el mismo formato del ejemplo del enunciado.

Lo probé en Windows. Ahí el modo sale como `100666` para archivos y `040777` para directorios, porque Windows no maneja los permisos como Linux y Python los aproxima.
