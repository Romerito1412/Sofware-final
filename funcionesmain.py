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
    print("Esta es la opciòn para registrar un estudiante")
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
                    "El dato ingresado no es un nùmero o es decimal, ingrese solo nùmeros enteros positivos"
                )
                continue
            else:
                if (
                    id.isdigit() and int(id) <= 999
                ):  # es decir un numero positvo entero y si es menor o igual a 999
                    for id_s in registro:
                        if id_s["id"] == id:
                            existe = True  # confirma que el id que ingresaste si existe
                            print("ID ya existente, pruebe otro ID")
                            continue
                else:
                    print(
                        "Ingreso un ID no valido, ingrese solo numeros enteros positivos e iguales o menores a 999"
                    )
                    continue
                if existe:
                    activo = True
                else:
                    activo = False
        activo = True  # sea crea activo para el loop de abajo
        while activo:  # Validacion del nombre
            nombre = input("Nombre >>> ").upper().strip()
            if nombre.isdigit():  # es decir un numero positvo entero
                print("Ingreso un nombre no valido, ingrese solo letras")
                continue
            else:
                activo = False  # cierra el ciclo y deja pasar al siguiente paso

        estudiante = {
            "id": id,
            "nombre": nombre,
        }  # Aquì se crea  el diccionario que se apendizarà al .Json basado en las varibles id y estudiante declaradas anteriormente
        registro.append(estudiante)

        print(
            f"Usted ha ingresado al estudiante {nombre} con el id {id}, esta correcto? S/cualquier otra letra"
        )
        decision = input().strip().upper()
        if decision == "S":  # preguntarle al usuario si estan correctos los datos
            with open(
                "registroestudiantes.json", "w", encoding="utf-8"
            ) as archivar:  # abrimos el archivo
                json.dump(  # esto es lo que se ingresarà al archivo
                    {
                        "Registro": registro,
                    },
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
    """docstring
    Este es el menù que se mostrarà si elijen la opcion 2, este servirà para ver 5 opciones de
    edicion mas y tambien una salida de ese menu"""
    activo = True
    while activo:
        print(
            "\n Bienvenido al contro de gastos para los estudiantes de la residencia [Nombre de la residencia]"
        )
        print("¡Què desea hacer?")
        for index, opciones in enumerate(opcionesmenuestudiantes):
            print(f"{index + 1}. {opciones}")
        opcionmenu = input().lower().strip()
        if opcionmenu == "1":
            activo = registrogasto()
        elif opcionmenu == "2":
            depositoahorro()
        elif opcionmenu == "3":
            agregarmetaahorro()
        elif opcionmenu == "4":
            retirodineroahorro()
        elif opcionmenu == "5":
            elimarregistrogsasto()
        elif opcionmenu == "6":
            salirmenu()
        else:
            print(
                f"La opciòn {opcionmenu} que ingreso no se encuentra en las opciones posibles \n vuelva a intentar"
            )


def mostrarregistro():
    with open("registroestudiantes.json", "r", encoding="utf-8") as registro:
        estudiantes = json.load(registro)["Registro"]

        with open("registrogastos.json", "r", encoding="utf-8") as registro_gasto:
            estudiante_gastos = json.load(registro_gasto)["Gastos"]

            # Por índice
            for estudiante in estudiantes:
                print(estudiante)  # primer registro

            # Por valor (ej: buscar por id)
            id = input(
                "Ingrese el id de estudiante para consultar su registro: "
            ).strip()
            for estudiante in estudiantes:
                if estudiante["id"] == id:
                    print(f"Nombre:{estudiante['nombre']}")
                    for gasto in estudiante_gastos:
                        if gasto["id"] == id:
                            print(f"id: {gasto['id']}")
                            for gastos in gasto["gastos"]:
                                print(gastos)
                                break


def eliminarregistro():
    """docstring
    Esta funcion sirve para elimiinar un registro previamente registrado
    """
    if registro:  # verifica si existe ya algun registro
        activo = True  # varibale creada para que el siguiente loop funcione
        contador = (
            0  # variable creada para saber el index del archivo a borrar si existe
        )
        while activo:
            print("Esta es la opciòn para registrar un estudiante")
            print(
                "Tiene que ingresar el id del registro que quiera eliminar (Fin para salir)"
            )
            time.sleep(2)
            mostrarestudiantes()
            identificacion = input("ID >>> ").strip().upper()
            if identificacion != "FIN":
                with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
                    textos = json.load(archivo)["Registro"]
                    for texto in textos:
                        if texto["id"] == identificacion:
                            existe = True
                            break
                    if existe:
                        print(
                            f"El ID {identificacion} pertene a al estudiante {texto['nombre']}, esta seguro de querer borrarlo? S/cualquier otro caracter"
                        )
                        decision = input("S/cualquier otra letra").strip().upper()
                        if decision == "S":
                            for texto in textos:
                                if texto["id"] == identificacion:
                                    remanente = textos.pop(contador)
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
                                            {
                                                "Registro": textos,
                                            },
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
                                else:
                                    contador += 1
                            print(textos)
                            input()
                        else:
                            continue
                    else:
                        print("Ese id no existe, pruebe otro")
            else:
                mensajesaliendo()
                activo = False
    else:
        print(
            "Aun no hay registros, vuelva cuando se haya registrado al menos un estudiante"
        )


def cerrarprograma():
    """docstring"""
    print("\nCerrando programa, ¡adiós!")
    return False
