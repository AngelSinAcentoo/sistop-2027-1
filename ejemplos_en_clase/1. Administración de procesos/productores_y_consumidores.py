#!/usr/bin/python3
import threading
import random
import time

num_prod = 4
num_cons = 3
cinta_max = 5
cinta = []
elementos = threading.Semaphore(0)
mutex = threading.Semaphore(1)
max_cinta = threading.Semaphore(cinta_max)

def msg(num, rol, msg):
    print(rol, num, '→', msg)

def productor(num):
    while True:
        msg(num, 'P', 'Produciendo')
        time.sleep(random.random())
        prod = random.random()
        msg(num, 'P', f'Listo! Enviando {prod}')
        max_cinta.acquire()
        with mutex:
            cinta.append(prod)
        elementos.release()

def consumidor(num):
    while True:
        msg(num, 'C', '¡Listo!')
        elementos.acquire()
        max_cinta.release()
        with mutex:
            cosa = cinta.pop()
        time.sleep(0.5)
        msg(num, 'C', f'Procesando cosa: {cosa}')

def monitor():
    while True:
        msg(0, 'M', f'{" "*50} Elementos en la lista: {len(cinta)}')
        time.sleep(0.5)

threading.Thread(target=monitor).start()

for i in range(num_prod):
    threading.Thread(target=productor, args=[i]).start()

for i in range(num_cons):
    threading.Thread(target=consumidor, args=[i]).start()
