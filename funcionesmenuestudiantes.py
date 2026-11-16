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
            activo = False
        else:
            mensajesaliendo()


def depositoahorro():
    pass


def agregarmetaahorro():
    pass


def retirodineroahorro():
    pass


def elimarregistrogsasto():
    pass


def salirmenu():
    pass
