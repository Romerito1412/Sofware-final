# documento para las clases
import json
import time

from funcionesextras import *
from listas import *

registro = validararchivosdetxt(
    "registrogastos.json", "Gastos"
)  # revisa si ya existe algun registro y crea una variable llamada registro


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
        while True:
            existe = "noseguir"  # variable creada para definir si la persona debe seguir el proceso o no
            with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
                estudiantes = json.load(archivo)["Registro"]
                print("Revisando registros...")
                time.sleep(1)
                for estudiante in estudiantes:
                    if self.id == estudiante["id"]:
                        existe = "siguiente"  # si el estudiante existe la persona puede seguir, sino se le preguntara si quiere agregar otro id
                        seleccionado = estudiante  # se guarda la informaciòn de la persona si  existe
                if existe == "siguiente":
                    print(
                        f"Ha elegido al estudiante {seleccionado['nombre'].title()} con el ID {seleccionado['id']}"
                    )
                    time.sleep(1)
                    activo = True
                    while activo:
                        print(
                            "en cuàl àrea quiere registrar el gasto? (seleccione el numero)"
                        )
                        contador = 0
                        for area in (
                            self.gastosregistro
                        ):  # se le muestran las 4 opciones existentes
                            contador += 1
                            print(f"{contador}. {area}")
                        decision = input("Area >>> ").strip()
                        if decision == "1":
                            # funcione si que sirve para ingresar el id, el area de gasto y la cantidad gastada para guardarla
                            activo = agregargastoarea(seleccionado, registro, "Comida")

                        elif decision == "2":
                            # funcione si que sirve para ingresar el id, el area de gasto y la cantidad gastada para guardarla
                            activo = agregargastoarea(
                                seleccionado, registro, "Transporte"
                            )
                        elif decision == "3":
                            # funcione si que sirve para ingresar el id, el area de gasto y la cantidad gastada para guardarla
                            activo = agregargastoarea(seleccionado, registro, "Salidas")
                        elif decision == "4":
                            activo = agregargastoarea(
                                # funcione si que sirve para ingresar el id, el area de gasto y la cantidad gastada para guardarla
                                seleccionado,
                                registro,
                                "Estudios",
                            )
                        else:
                            print("Esa opcion no exsite, pruebe otra")
                            continue
                    break
                else:
                    print("Este estudiante no existe, pruebe otro id.")
                    time.sleep(1)
                    break

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
