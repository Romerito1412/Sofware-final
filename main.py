# Proyexto final software - Documento principal

import listas
from funciones import *

activo = True

while activo:
    print(
        "Bienvenido al contro de gastos para los estudiantes de la residencia [Nombre de la residencia]"
    )
    print("¡Què desea hacer?")
    for index, opciones in enumerate(listas.opciones):
        print(f"{index + 1}. {opciones}")
    opcionmenu = input().lower().strip()
    if opcionmenu == "1":
        registrarestudiante()
    elif opcionmenu == "2":
        menuestudiantes()
    elif opcionmenu == "3":
        mostrarregistro()
    elif opcionmenu == "4":
        eliminarregistro()
    elif opcionmenu == "5":
        cerrarprograma()
    else:
        print(
            f"La opciòn {opcionmenu} que ingreso no se encuentra en las opciones posibles \n vuelva a intentar"
        )
