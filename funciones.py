# documento para las funciones

from clases import *
from listas import *


def registrarestudiante():
    """docstring"""
    print("Esta es la opciòn para registrar un estudiante")
    print("Tiene que ingresar lo siguiente")
    for i in estudintedatos:
        print(i)
    id = input("ID").upper().split()
    nombre = input("Nombre").upper().split()

    with open("registroestudiantes.json", "a", encoding="uft-8") as registro:
        registrarestudiante(id, nombre)


def menuestudiantes():
    """docstring"""


def mostrarregistro():
    """docstring"""


def eliminarregistro():
    """docstring"""


def cerrarprograma():
    """docstring"""
