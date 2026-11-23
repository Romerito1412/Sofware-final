import json
import time


def validararchivosdetxt(archivotxt, clave):
    """Esta funncion se conecta a travez de funcionesmenuestudiantes y funcionesmain que sirven
    para verificar si algun registre ya existe en el archivo, si no existe crea una lista vacia llamada
    registro, si sì existe crea la variable registro y tambièn le agrega todo lo que ya tiene el json
    se le ingresan dos parametros, uno con el nombre del archivo y el otro con el keyvalue para acceder
    al registro si sì existe"""
    try:
        with open(archivotxt, "r", encoding=("utf-8")) as datos:
            return json.load(datos)[clave]
    except (FileNotFoundError, json.decoder.JSONDecodeError, KeyError):
        return []


def mensajesaliendo():
    """Es un mensaje dicien que estas saliendo de una opcion"""
    print("Saliendo de esta opción...")
    time.sleep(1)
    print("...")
    time.sleep(1)


def mostrarestudiantes():
    """Esta funcion muestra a los estudiantes con su nombre y ID"""
    print("Estos son los IDs registrados")
    try:
        with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
            textos = json.load(archivo)["Registro"]
            for texto in textos:
                print(f"ID: {texto['id']}, Nombre: {texto['nombre']}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Aún no hay estudiantes registrados.")


def agregargastoarea(seleccionado, registro, area):
    """Esta funcion sirve para agregar un gasto al json de registro de gastos con el ID de la persona
    el area donde lo gasto y cuanto gasto
    se le ingresan los parametros de un diccionario con el ID y nombre de la persona, el registrod e gastos y tambien
    el area donde gasto el dinero"""
    print("Elija la cantidad de dinero a registrar")
    cant = input("Cantidad (en $) >>> ").strip()
    try:
        cant = float(cant)
    except ValueError:
        print("Solo puede ingresar números positivos mayores a 0")
        return True
    if cant <= 0:
        print("Solo puede ingresar números positivos mayores a 0")
        return True

    print(
        f"Usted esta ingresando {cant}$ al estudiante {seleccionado['nombre'].title()}, ID: {seleccionado['id']}"
    )

    # Buscar si ya existe un registro para este id
    encontrado = None
    for item in registro:
        if item["id"] == seleccionado["id"]:
            encontrado = item
            break

    if encontrado is None:
        encontrado = {"id": seleccionado["id"], "gastos": {}}
        registro.append(encontrado)

    if area not in encontrado["gastos"]:
        encontrado["gastos"][area] = []
    encontrado["gastos"][area].append(cant)

    with open("registrogastos.json", "w", encoding="utf-8") as archivo:
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