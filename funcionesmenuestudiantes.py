from clases import *
from funcionesextras import *


def registrogasto():
    activo_3 = True
    print("Bienvenido, estás a punto de registrar un gasto")
    while activo_3:
        print(
            "Selecciona el ID del estudiante al que le registrarás un gasto (FIN para terminar)"
        )
        time.sleep(1.5)
        mostrarestudiantes()
        opcion = input("ID >>> ").strip().upper()
        if opcion != "FIN":
            Registrosgasto(opcion).agregargasto()
        else:
            mensajesaliendo()
            activo_3 = False


def depositoahorro():
    activo_3 = True
    print("Bienvenido. Estás a punto de registrar un ahorro")
    while activo_3:
        print(
            "Selecciona el ID del estudiante al que le registrarás un ahorro (FIN para terminar)"
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
    print("Bienvenido. Estás a punto de establecer una meta de ahorro")
    while activo_3:
        print(
            "Selecciona el ID del estudiante al que le establecerás una meta (FIN para terminar)"
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
    print("Bienvenido. Estás a punto de retirar dinero de los ahorros")
    while activo_3:
        print(
            "Selecciona el ID del estudiante al que le retirarás dinero (FIN para terminar)"
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
    print("Bienvenido, estás a punto de eliminar un gasto")
    while activo_3:
        print(
            "\nSelecciona el ID del estudiante al que le eliminarás un gasto (FIN para terminar)"
        )
        mostrarestudiantes()
        opcion = input("ID >>> ").strip().upper()

        if opcion != "FIN":
            try:
                Registrosgasto(opcion).eliminargasto()
            except Exception as e:
                print(f"\nOcurrió un error inesperado: {e}")
                input("Presione Enter para continuar...")
            mensajesaliendo()
            activo_3 = False
        else:
            mensajesaliendo()
            activo_3 = False


def salirmenu():
    mensajesaliendo()
    return False
