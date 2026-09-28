#!/usr/bin/python
import os
import time
NUM = 5

pid = os.fork()
if pid > 0:
    # Proceso padre
    time.sleep(1)
    print(f"Proceso padre. Mi número mágico es: #{NUM}")
elif pid == 0:
    # Proceso hijo
    NUM = 0
    print(f"Proceso hijo. Mi número mágico es: #{NUM}")
else:
    print("No se qué pasó, pero no debía haber ocurrido")
