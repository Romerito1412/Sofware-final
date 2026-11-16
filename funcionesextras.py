import json
import time


def validararchivosdetxt(archivotxt, clave):
    try:
        with open(archivotxt, "r", encoding=("utf-8")) as registro:
            json.load(registro)
    except json.decoder.JSONDecodeError:
        return []
    else:
        with open(archivotxt, "r", encoding=("utf-8")) as datos:
            return json.load(datos)[clave]


def mensajesaliendo():
    print("saliendo de esta opciòn...")
    time.sleep(1)
    print("...")
    time.sleep(1)


def mostrarestudiantes():
    print("estos son los ID`s registrados")
    with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
        textos = json.load(archivo)["Registro"]
        for texto in textos:
            print(f"ID: {texto['id']}, Nombre: {texto['nombre']}")
