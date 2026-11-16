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


def agregargastoarea(seleccionado, registro, area):
    print("Elija la cantidad de dinero a registrar")
    cant = input("Cantidad (en $) >>> ").strip()
    try:
        cant = float(cant)
    except ValueError:
        print("Solo puede ingresar numeros positivos")
    else:
        if cant >= 0:
            print(
                f"Usted esta ingresando {cant}$ al estudiante {seleccionado['nombre'].title()}, ID: {seleccionado['id']}"
            )
            with open("registrogastos.json", "w", encoding="utf-8") as archivo:
                registro.append(  # [{dict}]
                    {
                        "id": seleccionado["id"],
                        "gastos": {
                            area: [],
                        },
                    }
                )
                registro[-1]["gastos"][area].append(cant)
                json.dump(
                    {"Gastos": registro},
                    archivo,
                    indent=2,
                    ensure_ascii=False,
                )
                print("guardando registro...")
                time.sleep(1)
                mensajesaliendo()
                return False
        else:
            print("solo puede ingresar numeros positivos")
            return True
