#!/usr/bin/python3
import threading
from colorama import Fore
from time import sleep
import random

SIMULT=4
JUGADORES=10
COLORES = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED,
           Fore.YELLOW, Fore.WHITE, Fore.LIGHTBLUE_EX, Fore.LIGHTBLACK_EX,
           Fore.LIGHTRED_EX]

multiplex = threading.Semaphore(SIMULT)
mensajes = 0
mutex = threading.Semaphore(1)

def msg(num, msg):
    global mensajes
    print(COLORES[num], msg, end='')
    mutex.acquire()
    mensajes += 1
    if mensajes % 10 == 0:
        print("")
    mutex.release()

def turno(num):
    msg(num, '↑')
    multiplex.acquire()
    for mov in range(random.randint(1,10)):
        msg(num, '•')
        sleep(random.random())
    multiplex.release()
    msg(num, '→')

for thr in range(JUGADORES):
    threading.Thread(target=turno, args=[thr]).start()
