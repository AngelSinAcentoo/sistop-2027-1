#!/usr/bin/python3
import threading
import time
import os

NUM = 10
threads = []

def funcion_hilo(num):
    print(f"Yo soy el hilo número {num} del proceso {os.getpid()} y te saludo con gusto.")
    time.sleep(1)

for i in range(NUM):
    threads.append(threading.Thread(target=funcion_hilo, args=[i]))

print(f"Tengo {NUM} hilos listos para iniciar su ejecución:")

for thr in threads:
    thr.start()

print("Los hilos están ejecutándose...")

for thr in threads:
    thr.join()

print(f"Los {NUM} hilos ya terminaron su ejecución")
