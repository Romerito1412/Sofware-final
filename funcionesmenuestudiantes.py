from clases import *
from funcionesextras import *


def registrogasto():
    """
    Esta funcion es llamada cuando se elije la opcion 1 del segundi menu, no toma ningun parametro
    y solo muestra mensajes y te pregunta un input, de ahi llama al metodo de agregargasto de la clase Registrosgastos
    """
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
            Registrosgasto(
                opcion
            ).agregargasto()  # a esta clase si se le agrega un parametro que es el ID
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
