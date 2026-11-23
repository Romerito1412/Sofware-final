import json
import time


def validararchivosdetxt(archivotxt, clave):
    """Esta funncion se conecta a travez de funcionesmenuestudiantes y funcionesmain que sirven
    para verificar si algun registre ya existe en el archivo, si no existe crea una lista vacia llamada
    registro, si sì existe crea la variable registro y tambièn le agrega todo lo que ya tiene el json
    se le ingresan dos parametros, uno con el nombre del archivo y el otro con el keyvalue para acceder
    al registro si sì existe"""
    try:
        with open(archivotxt, "r", encoding=("utf-8")) as registro:
            json.load(registro)
    except json.decoder.JSONDecodeError:
        return []
    else:
        with open(archivotxt, "r", encoding=("utf-8")) as datos:
            return json.load(datos)[clave]


def mensajesaliendo():
    """Es un mensaje dicien que estas saliendo de una opcion"""
    print("Saliendo de esta opción...")
    time.sleep(1)
    print("...")
    time.sleep(1)


def mostrarestudiantes():
    """Esta funcion muestra a los estudiantes con su nombre y ID"""
    print("\n")
    print("Estos son los ID`s registrados")
    with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
        textos = json.load(archivo)["Registro"]
        for texto in textos:
            print(f"ID: {texto['id']}, Nombre: {texto['nombre']}")


def agregargastoarea(seleccionado, registro, area):
    """Esta funcion sirve para agregar un gasto al json de registro de gastos con el ID de la persona
    el area donde lo gasto y cuanto gasto
    se le ingresan los parametros de un diccionario con el ID y nombre de la persona, el registrod e gastos y tambien
    el area donde gasto el dinero"""
    while True:
        print("Elija la cantidad de dinero a registrar")
        cant = input("Cantidad (en $) >>> ").strip()
        try:
            cant = float(cant)
        except ValueError:
            print("Solo puede ingresar números positivos")
        else:
            if cant >= 0:
                print(
                    f"\n  -Usted esta ingresando {cant}$ al estudiante {seleccionado['nombre'].title()}, ID: {seleccionado['id']}\n"
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
                print("Solo puede ingresar números positivos")
                return True
