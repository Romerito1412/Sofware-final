# documento para las funciones

import json
import time

from clases import *
from funcionesextras import *
from funcionesmenuestudiantes import *
from listas import *

registro = validararchivosdetxt("registroestudiantes.json", "Registro")
eliminados = validararchivosdetxt("registroeliminados.json", "HistorialEliminados")


def registrarestudiante():
    """Esta funcion registra el ID y el nombre de un estudiante para luego agregarlo a un archivo .Json donde se mete dentre de
    un diccionario con el nombre `Registro` donde hay una lista con todos los reegistroos ya hechos"""
    print("Esta es la opción para registrar un estudiante")
    while True:
        print("Tiene que ingresar lo siguiente")
        for i in estudintedatos:
            print(i)
        activo = True
        while activo:  # Validacion del id y ver si tiene repeticion
            existe = False
            id = input("ID >>> ").strip()
            try:
                validacion = int(id)
            except ValueError:
                print(
                    "El dato ingresado no es un número o es decimal, ingrese solo números enteros positivos"
                )
                continue
            else:
                if id.isdigit() and int(id) <= 999:
                    for id_s in registro:
                        if id_s["id"] == id:
                            existe = True
                            print("ID ya existente, pruebe otro ID")
                            break
                else:
                    print(
                        "Ingresó un ID no válido, ingrese solo números enteros positivos e iguales o menores a 999"
                    )
                    continue
                if existe:
                    activo = True
                else:
                    activo = False
        activo = True
        while activo:  # Validacion del nombre
            nombre = input("Nombre >>> ").upper().strip()
            if nombre.isdigit():
                print("Ingresó un nombre no válido, ingrese solo letras")
                continue
            else:
                activo = False

        estudiante = {"id": id, "nombre": nombre}

        print(
            f"Usted ha ingresado al estudiante {nombre} con el id {id}, esta correcto? S/cualquier otra letra"
        )
        decision = input().strip().upper()
        if decision == "S":
            registro.append(estudiante)
            with open(
                "registroestudiantes.json", "w", encoding="utf-8"
            ) as archivar:
                json.dump(
                    {"Registro": registro},
                    archivar,
                    indent=2,
                    ensure_ascii=False,
                )
            print("Guardando registro...")
            time.sleep(1)
            mensajesaliendo()
            break
        else:
            print("Vuelva a ingresar los datos")


def menuestudiantes():
    #Menú de opción 2
    activo = True
    while activo:
        print(
            "\n Bienvenido al control de gastos para los estudiantes"
        )
        print("¿Qué deseas hacer? Escoge el número de la opción: ")
        for index, opciones in enumerate(opcionesmenuestudiantes):
            print(f"{index + 1}. {opciones}")
        opcionmenu = input().lower().strip()
        if opcionmenu == "1":
            registrogasto()
        elif opcionmenu == "2":
            depositoahorro()
        elif opcionmenu == "3":
            agregarmetaahorro()
        elif opcionmenu == "4":
            retirodineroahorro()
        elif opcionmenu == "5":
            elimarregistrogsasto()
        elif opcionmenu == "6":
            activo = salirmenu()
        else:
            print(
                f"El número {opcionmenu} no existe en las opciones posibles \n Vuelva a intentar :)"
            )


def mostrarregistro():
    """
    Esta función servirá para buscar todos los registros o buscar uno es específico
    """
    estudiantes = validararchivosdetxt("registroestudiantes.json", "Registro")
    estudiante_gastos = validararchivosdetxt("registrogastos.json", "Gastos")
    estudiante_ahorro = validararchivosdetxt("registroahorros.json", "Ahorros")

    import clases as c

    activo = True
    while activo == True:
        print("\n1. Buscar un registro de estudiante por id")
        print("2. Consultar registro general de gastos")
        consulta = input("Digite la opción que desea realizar (FIN para salir): ").strip().upper()
        if consulta == "1":
            # Por valor (ej: buscar por id)
            activo_2 = True
            while activo_2 == True:
                for estudiante in estudiantes:
                    print(f"ID: {estudiante['id']}, Nombre: {estudiante['nombre']}")
                id_estudiante = input(
                    "\nIngrese el id de estudiante para consultar su registro (FIN para salir): "
                ).strip()

                if id_estudiante.strip().upper() == "FIN":
                    mensajesaliendo()
                    break

                encontrado = False
                for estudiante in estudiantes:
                    if estudiante["id"] == id_estudiante.strip():
                        print(f"\nNombre:{estudiante['nombre']}")
                        print(f"id: {estudiante['id']}")
                        encontrado = True
                        break

                if not encontrado:
                    print("\nid inválido")
                else:
                    registro_est = c.Registrosgasto(id_estudiante)

                    for gasto in estudiante_gastos:
                        if gasto["id"] == id_estudiante:
                            for categoria, montos in gasto["gastos"].items():
                                if categoria in registro_est.gastosregistro:
                                    for monto in montos:
                                        registro_est.gastosregistro[categoria].append(
                                            monto
                                        )

                    total = 0
                    for categoria, lista in registro_est.gastosregistro.items():
                        total += sum(lista)

                    ahorro_encontrado = False
                    for ahorro in estudiante_ahorro:
                        if ahorro["id"] == id_estudiante:
                            ahorro_encontrado = True

                    if total == 0 and not ahorro_encontrado:
                        print("\nNo se encontraron registros de gastos o ahorros")
                    else:
                        if total == 0:
                            print("\nNo se encontraron registros de gastos")
                        else:
                            print("\nGastos:")
                            for (
                                categoria,
                                lista,
                            ) in registro_est.gastosregistro.items():
                                print(f" {categoria}: {sum(lista)}")
                            print(f"\nTotal: {total}")

                        if not ahorro_encontrado:
                            print("\nNo se encontraron registros de ahorros\n")
                        else:
                            print("\nAhorros:")
                            for ahorro in estudiante_ahorro:
                                if ahorro["id"] == id_estudiante:
                                    print(f"Meta: {ahorro['Meta']}")
                                    print(
                                        f"Dinero requerido: {ahorro['Dinerorequerido']}"
                                    )
                                    print(
                                        f"Dinero actual: {ahorro['Dineroactual']}"
                                    )
                time.sleep(5)

        elif consulta == "2":
            registro_general = c.Registrosgasto("general")

            for gasto in estudiante_gastos:
                for categoria, montos in gasto["gastos"].items():
                    if categoria in registro_general.gastosregistro:
                        for monto in montos:
                            registro_general.gastosregistro[categoria].append(monto)

            total = 0
            for categoria, lista in registro_general.gastosregistro.items():
                total += sum(lista)

            if total == 0:
                print("\nNo se encontraron registros de gastos")
            else:
                print("\nGastos generales:")
                for categoria, lista in registro_general.gastosregistro.items():
                    print(f" {categoria}: {sum(lista)}")
                print(f"\nTotal general: {total}")

            total_ahorrado = 0

            for ahorro in estudiante_ahorro:
                total_ahorrado += ahorro["Dineroactual"]

            if total_ahorrado == 0:
                print("\nNo se encontraron registros de ahorros")
            else:
                print("\nAhorros:")
                print(f" Dinero actual total: {total_ahorrado}")

        elif consulta == "FIN":
            mensajesaliendo()
            break
        else:
            print("\nDigite porfavor una opción valida (1-3)")


def eliminarregistro():
    """ 
    Esta funcion sirve para eliminar un registro previamente registrado
    """
    if registro:  # verifica si existe ya algun registro
        activo = True
        while activo:
            print("Esta es la opción para eliminar un estudiante")
            print(
                "Tiene que ingresar el id del registro que quiera eliminar (Fin para salir)"
            )
            time.sleep(2)
            mostrarestudiantes()
            identificacion = input("ID >>> ").strip().upper()
            if identificacion != "FIN":
                existe = False
                with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
                    textos = json.load(archivo)["Registro"]
                for texto in textos:
                    if texto["id"] == identificacion:
                        existe = True
                        print(
                            f"El ID {identificacion} pertenece al estudiante {texto['nombre']}, esta seguro de querer borrarlo? S/cualquier otro caracter"
                        )
                        decision = input("S/cualquier otra letra >>> ").strip().upper()
                        if decision == "S":
                            indice = textos.index(texto)
                            remanente = textos.pop(indice)
                            print("Eliminando registro...")
                            time.sleep(1)
                            print("Registro eliminado")
                            time.sleep(1)
                            with open(
                                "registroestudiantes.json",
                                "w",
                                encoding="utf-8",
                            ) as archivo:
                                json.dump(
                                    {"Registro": textos},
                                    archivo,
                                    indent=2,
                                    ensure_ascii=False,
                                )
                            with open(
                                "registroeliminados.json", "w", encoding="utf-8"
                            ) as archivo:
                                eliminados.append(remanente)
                                json.dump(
                                    {"HistorialEliminados": eliminados},
                                    archivo,
                                    indent=2,
                                    ensure_ascii=False,
                                )
                            return
                        break
                if not existe:
                    print("Ese id no existe, pruebe otro")
            else:
                mensajesaliendo()
                activo = False
    else:
        print(
            "Aun no hay registros, vuelva cuando se haya registrado al menos un estudiante"
        )


def cerrarprograma():
    print("\nCerrando programa, ¡adiós!")
    return False