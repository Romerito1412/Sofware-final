# documento para las funciones
def registrarestudiante():
    """docstring"""


def menuestudiantes():
    """docstring"""
    activo = True

    while activo:
        import listas
        print(
            "Bienvenido al contro de gastos para los estudiantes de la residencia [Nombre de la residencia]"
        )
        print("¡Què desea hacer?")
        for index, opciones in enumerate(listas.opciones02):
            print(f"{index + 1}. {opciones}")
        opcionmenu = input().lower().strip()
        if opcionmenu == "1":
            #agregargasto()
            pass
        elif opcionmenu == "2":
            #agregarahorro()
            pass
        elif opcionmenu == "3":
            #agregarmeta()
            pass
        elif opcionmenu == "4":
            #quitargasto()
            pass
        elif opcionmenu == "5":
            #quitarahorro()
            pass
        elif opcionmenu == "6":
            #salir()
            pass
        else:
            print(
                f"La opciòn {opcionmenu} que ingreso no se encuentra en las opciones posibles \n vuelva a intentar"
            )


def mostrarregistro():
    """docstring"""


def eliminarregistro():
    """docstring"""


def cerrarprograma():
    """docstring"""
