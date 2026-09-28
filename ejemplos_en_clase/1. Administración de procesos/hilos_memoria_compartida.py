#!/usr/bin/python
import threading

NUM = 5

def modifica_variable():
    global NUM
    NUM = 0
    print(f"Hilo hijo. Mi número mágico es: #{NUM}")


print(f"Antes de lanzar el hilo, mi número mágico es {NUM}")
thr = threading.Thread(target=modifica_variable, args=[])
thr.start()
thr.join()

print(f"Hilo padre. Mi número mágico es: #{NUM}")
