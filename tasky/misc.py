import os
import sys
import tty
import termios

def limpiarPantalla(): #Limpiar pantalla, Linux/Windows
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def getchr(prompt=''): #presionar una tecla para continuar, Linux/Windows
    """lee un solo carácter"""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
