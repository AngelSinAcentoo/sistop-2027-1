#!/usr/bin/python3
import os
import sys
import time

if len(sys.argv) != 3 or not sys.argv[2].isdigit() or not os.path.isdir(sys.argv[1]):
    print(f'Invocación: {sys.argv[0]} <directorio> <días>')
    exit(1)

directorio = sys.argv[1]
dias = int(sys.argv[2])
limite = time.time() - dias * 24 * 60 * 60

archivos = []
with os.scandir(directorio) as dir:
    for archivo in dir:
        info = archivo.stat(follow_symlinks=False)
        if info.st_mtime >= limite:
            archivos.append((archivo.name, info))

print(f'{"Nombre":30} {"Modificación":16} {"Modo":6} Tamaño')
print('=' * 62)
for nombre, info in sorted(archivos):
    fecha = time.strftime('%Y-%m-%d %H:%M', time.localtime(info.st_mtime))
    print(f'{nombre:30} {fecha} {info.st_mode:06o} {info.st_size}')
