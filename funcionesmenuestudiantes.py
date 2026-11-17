from clases import *
from funcionesextras import *


def registrogasto():
    activo_3 = True
    print("Bienvenido. estas a punto de registrar un gasto")
    while activo_3:
        print(
            "Seleciona el ID del estudiante al que le registraras un gasto (FIN para terminar)"
        )
        mostrarestudiantes()
        opcion = input("ID >>> ").strip().upper()
        if opcion != "FIN":
            Registrosgasto(opcion).agregargasto()
        else:
            mensajesaliendo()
            activo_3 = False


def depositoahorro():
    activo_3 = True
    print("Bienvenido. estas a punto de registrar un ahorro")
    while activo_3:
        print(
            "Seleciona el ID del estudiante al que le registraras un ahorro (FIN para terminar)"
        )
        mostrarestudiantes()
        opcion = input("ID >>> ").strip().upper()
        if opcion != "FIN":
            Registrosgasto(opcion).agregarahorro()
            activo_3 = False
        else:
            mensajesaliendo()
            activo_3 = False
        


def agregarmetaahorro():
    activo_3 = True
    print("Bienvenido. estas a punto de establecer una meta de ahorro")
    while activo_3:
        print(
            "Seleciona el ID del estudiante al que le estableceras una meta (FIN para terminar)"
        )
        mostrarestudiantes()
        opcion = input("ID >>> ").strip().upper()
        if opcion != "FIN":
            Registrosgasto(opcion).agregarmeta()
        else:
            mensajesaliendo()
            activo_3 = False


def retirodineroahorro():
    activo_3 = True
    print("Bienvenido. estas a punto de retirar dinero de los ahorros")
    while activo_3:
        print(
            "Seleciona el ID del estudiante al que le retiraras dinero (FIN para terminar)"
        )
        mostrarestudiantes()
        opcion = input("ID >>> ").strip().upper()
        if opcion != "FIN":
            Registrosgasto(opcion).eliminarahorro()
        else:
            mensajesaliendo()
            activo_3 = False


def elimarregistrogsasto():
    activo_3 = True
    print("Bienvenido. estas a punto de eliminar un gasto")
    while activo_3:
        print(
            "Seleciona el ID del estudiante al que le eliminaras un gasto (FIN para terminar)"
        )
        mostrarestudiantes()
        opcion = input("ID >>> ").strip().upper()
        if opcion != "FIN":
            Registrosgasto(opcion).eliminargasto()
        else:
            mensajesaliendo()
            activo_3 = False


def salirmenu():
        mensajesaliendo()
        return False
