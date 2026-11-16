from clases import *
from funcionesextras import *


def registrogasto():
    activo = True
    print("Bienvenido. estas a punto de registrar un gasto")
    while activo:
        print(
            "Seleciona el ID del estudiante al que le registraras un gasto (FIN para terminar)"
        )
        time.sleep(2)
        mostrarestudiantes()

        opcion = input("ID >>> ").strip().upper()
        if opcion != "FIN":
            Registrosgasto(opcion).agregargasto()
        else:
            mensajesaliendo()


def depositoahorro():
    activo = True
    while activo:
        print(
            "Seleciona el ID del estudiante al que le registraras un ahorro (FIN para terminar)"
        )
        opcion = input("ID >>> ").strip().upper()
        if opcion != "FIN":
            Registrosgasto(opcion).agregarahorro()
        else:
            mensajesaliendo()
            activo = False
        


def agregarmetaahorro():
    activo = True
    print("Bienvenido. estas a punto de retirar dinero de los ahorros")
    while activo:
        print(
            "Seleciona el ID del estudiante al que le retiraras dinero (FIN para terminar)"
        )
        opcion = input("ID >>> ").strip().upper()
        if opcion != "FIN":
            Registrosgasto(opcion).eliminarahorro()
        else:
            mensajesaliendo()
            activo = False


def retirodineroahorro():
    activo = True
    print("Bienvenido. estas a punto de retirar dinero de los ahorros")
    while activo:
        print(
            "Seleciona el ID del estudiante al que le retiraras dinero (FIN para terminar)"
        )
        opcion = input("ID >>> ").strip().upper()
        if opcion != "FIN":
            Registrosgasto(opcion).eliminarahorro()
        else:
            mensajesaliendo()
            activo = False


def elimarregistrogsasto():
    activo = True
    print("Bienvenido. estas a punto de eliminar un gasto")
    while activo:
        print(
            "Seleciona el ID del estudiante al que le eliminaras un gasto (FIN para terminar)"
        )
        opcion = input("ID >>> ").strip().upper()
        if opcion != "FIN":
            Registrosgasto(opcion).eliminargasto()
        else:
            mensajesaliendo()
            activo = False


def salirmenu():
    mensajesaliendo()
