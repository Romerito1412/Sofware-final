# documento para las clases
import json
import time

from funcionesextras import *
from listas import *

registro = validararchivosdetxt("registrogastos.json", "Gastos")


class Registrosgasto:
    """_summary"""

    def __init__(self, id):
        self.id = id
        self.nombre = ""
        self.gastosregistro = {
            "Comida": [],
            "Transporte": [],
            "Salidas": [],
            "Estudios": [],
        }
        self.ahorros = {"Meta": "", "Dinerorequerido": 0, "Dineroactual": 0}

    def agregargasto(self):
        existe = "noseguir"
        while True:
            with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
                estudiantes = json.load(archivo)["Registro"]
                print("Revisando registros...")
                time.sleep(1)
                for estudiante in estudiantes:
                    if self.id == estudiante["id"]:
                        existe = "siguiente"
                        seleccionado = estudiante
                if existe == "siguiente":
                    print(
                        f"Ha elegido al estudiante {seleccionado['nombre'].title()} con el ID {seleccionado['id']}"
                    )
                    time.sleep(1)
                    while True:
                        print(
                            "en cuàl àrea quiere registrar el gasto? (seleccione el numero)"
                        )
                        contador = 0
                        for area in self.gastosregistro:
                            contador += 1
                            print(f"{contador}. {area}")
                        decision = input("Area >>> ").strip()
                        if decision == "1":
                            area = "Comida"
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
                                    with open(
                                        "registrogastos.json", "w", encoding="utf-8"
                                    ) as archivo:
                                        registro.append(  # [{dict}]
                                            {
                                                "id": seleccionado["id"],
                                                "gastos": {
                                                    "Comida": [],
                                                },
                                            }
                                        )
                                        registro[-1]["gastos"]["Comida"].append(cant)
                                        json.dump(
                                            {"Gastos": registro},
                                            archivo,
                                            indent=2,
                                            ensure_ascii=False,
                                        )
                                        print("guardando registro...")
                                        time.sleep(1)
                                        mensajesaliendo()
                                        return
                                else:
                                    print("solo puede ingresar numeros positivos")

                        elif decision == "2":
                            print("ya ve 1")
                        elif decision == "3":
                            print("ya ve2 ")
                        elif decision == "4":
                            print("ya ve 3")
                        else:
                            print("Esa opcion no exsite, pruebe otra")
                            continue
                else:
                    print("Este estudiante no existe, pruebe otro id")

    def eliminargasto(self):
        pass

    def agregarahorro(self):
        pass

    def eliminarahorro(self):
        pass


class Registrogasto:
    """_summary"""

    def __init__(self):
        pass


class Registroahorro:
    """_summary"""

    def __init__(self):
        pass


class Registro:
    """_summary"""

    def __init__(self):
        pass
