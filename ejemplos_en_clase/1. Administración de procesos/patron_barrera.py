#!/usr/bin/python3
from threading import Semaphore, Thread
import random
import time

num_hilos = 10
cuenta = 0
mutex = Semaphore(1)
barrera = Semaphore(0)

def inicializa_estado(num):
    print(f'Hilo {num} inicializando...')
    time.sleep(random.random())
    print(f'Hilo {num} listo')

def trabajo_hilo(num):
    global cuenta
    inicializa_estado(num)

    mutex.acquire()
    cuenta = cuenta + 1

    if cuenta == num_hilos:
        barrera.release()
    mutex.release()

    barrera.acquire()
    barrera.release()

    print(f'Hilo {num} procesando!')

for i in range(3 * num_hilos):
    Thread(target=trabajo_hilo, args=[i]).start()
