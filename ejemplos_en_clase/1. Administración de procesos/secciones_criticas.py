#!/usr/bin/python3
import threading
from time import sleep
from random import random
contador = 0
color = 'azul'
mutex_cont = threading.Lock()
mutex_col = threading.Lock()

def establece_color(destino):
    global contador
    global color
    sleep(random())
    with mutex_cont:
        contador = contador + 1
    with mutex_col:
        color = destino
        sleep(random())
        with mutex_cont:
            print(f'El color ha sido modificado {contador} veces. El color ahora es {color}')

for c in ['rojo', 'azul', 'verde', 'negro', 'blanco']:
    threading.Thread(target=establece_color, args=[c]).start()
