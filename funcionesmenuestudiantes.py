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
            print("quiere agregar otro registro? S/cualquier otro caracter")
            decision = input(">>> ").strip().upper()
            if decision == "S":
                activo = True
            else:
                mensajesaliendo()
                return True
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
    print("\n¡Saliendo del menu!")
    activo = False
