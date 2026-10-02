#!/usr/bin/python3
import threading
import time
import random

sem1 = threading.Semaphore(0)
sem2 = threading.Semaphore(0)

def f1():
    demora = random.random()
    print(f'f1 entrando en t={time.time()}; demorando {demora}')
    time.sleep(demora)
    sem1.release()
    print(f'f1 ya mandó la señal en {time.time()}')
    sem2.acquire()
    print(f'f1 continuando, t={time.time()}')

def f2():
    demora = random.random()
    print(f'f2 entrando en t={time.time()}; demorando {demora}')
    time.sleep(demora)
    print(f'f2 ya mandó la señal en {time.time()}')
    sem2.release()
    sem1.acquire()
    print(f'f2 continuando, t={time.time()}')

threading.Thread(target=f1).start()
threading.Thread(target=f2).start()
