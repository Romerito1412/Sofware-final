# documento para las clases
import json
import time

from funcionesextras import *
from listas import *
registroahorros = validararchivosdetxt("registroahorros.json", "Ahorros")

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
        existe = False
        with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
            estudiantes = json.load(archivo)["Registro"]
            print("Revisando registros...")
            time.sleep(1)
            for estudiante in estudiantes:
                if self.id == estudiante["id"]:
                    existe = True
                    seleccionado = estudiante
                    break
        if existe:
            encontrado = None
            for item in registro:
                if item["id"] == seleccionado["id"]:
                    encontrado = item
                    break
            if encontrado:
                while True:
                    print("En cual area quiere eliminar el gasto?")
                    for contador, area in enumerate(areasgastos, start=1):
                        print(f"{contador}. {area}: {encontrado['gastos'][area]}")
                    decision = input("Area >>> ").strip()
                    if decision in ["1", "2", "3", "4"]:
                        area = areasgastos[int(decision) - 1]
                        lista_area = encontrado["gastos"][area]
                        if not lista_area:
                            print("No hay gastos registrados en esta area")
                            break
                        for i, monto in enumerate(lista_area, start=1):
                            print(f"{i}. ${monto}")
                        indice = input("Seleccione el numero del gasto a borrar >>> ").strip()
                        if indice.isdigit() and 1 <= int(indice) <= len(lista_area):
                            eliminado = lista_area.pop(int(indice) - 1)
                            with open(
                                "registrogastos.json", "w", encoding="utf-8"
                            ) as archivo:
                                json.dump(
                                    {"Gastos": registro},
                                    archivo,
                                    indent=2,
                                    ensure_ascii=False,
                                )
                            print(f"Gasto de ${eliminado} eliminado...")
                            time.sleep(1)
                            mensajesaliendo()
                            break
                        else:
                            print("Esa opcion no existe, pruebe otra")
                    else:
                        print("Esa opcion no existe, pruebe otra")
            else:
                print("Este estudiante no tiene gastos registrados")
        else:
            print("Este estudiante no existe, pruebe otro id")
    
    def agregarmeta(self):
        existe = False
        with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
            estudiantes = json.load(archivo)["Registro"]
            print("Revisando registros...")
            time.sleep(1)
            for estudiante in estudiantes:
                if self.id == estudiante["id"]:
                    existe = True
                    seleccionado = estudiante
                    break
        if existe:
            print(
                f"Ha elegido al estudiante {seleccionado['nombre'].title()} con el ID {seleccionado['id']}"
            )
            registro_previo = None
            for item in registroahorros:
                if item["id"] == seleccionado["id"]:
                    registro_previo = item
                    break

            if registro_previo and registro_previo["Meta"] != "":
                print(
                    f"Meta actual: '{registro_previo['Meta']}' por ${registro_previo['Dinerorequerido']} (Ahorrado: ${registro_previo['Dineroactual']})"
                )
                
            while True:
                meta = input("Por que esta ahorrando? (Nombre de la meta) >>> ").strip()
                cant = input("Cantidad de dinero que quisiera ahorrar (en $) >>> ").strip()
                try:
                    cant = float(cant)
                except ValueError:
                    print("Solo puede ingresar numeros positivos")
                else:
                    if cant > 0 and meta != "":
                        if registro_previo:
                            registro_previo["Meta"] = meta
                            registro_previo["Dinerorequerido"] = cant
                        else:
                            registroahorros.append(
                                {
                                    "id": seleccionado["id"],
                                    "Meta": meta,
                                    "Dinerorequerido": cant,
                                    "Dineroactual": 0.0,
                                }
                            )
                        with open(
                            "registroahorros.json", "w", encoding="utf-8"
                        ) as archivo:
                            json.dump(
                                {"Ahorros": registroahorros},
                                archivo,
                                indent=2,
                                ensure_ascii=False,
                            )
                        print("Guardando meta de ahorro...")
                        time.sleep(1)
                        mensajesaliendo()
                        break
                    else:
                        print("Datos no validos, vuelva a intentar")
        else:
            print("Este estudiante no existe, pruebe otro id")

    def agregarahorro(self):
        existe = False
        with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
            estudiantes = json.load(archivo)["Registro"]
            print("Revisando registros...")
            time.sleep(1)
            for estudiante in estudiantes:
                if self.id == estudiante["id"]:
                    existe = True
                    seleccionado = estudiante
                    break
        if existe:
            encontrado = None
            for item in registroahorros:
                if item["id"] == seleccionado["id"]:
                    encontrado = item
                    break
            if encontrado and encontrado["Meta"] != "":
                print(f"Meta actual: {encontrado['Meta']}")
                print(
                    f"Llevas ahorrado: ${encontrado['Dineroactual']} de ${encontrado['Dinerorequerido']}"
                )
                while True:
                    cant = input("¿Cuánto dinero deseas ingresar a tu ahorro? (en $) >>> ").strip()
                    try:
                        cant = float(cant)
                    except ValueError:
                        print("Solo puede ingresar numeros positivos")
                    else:
                        if cant > 0:
                            anterior = encontrado["Dineroactual"]
                            encontrado["Dineroactual"] += cant
                            with open(
                                "registroahorros.json", "w", encoding="utf-8"
                            ) as archivo:
                                json.dump(
                                    {"Ahorros": registroahorros},
                                    archivo,
                                    indent=2,
                                    ensure_ascii=False,
                                )
                            print(
                                f"Antes tenías ${anterior} y agregaste ${cant}."
                            )
                            print(
                                f"Llevas ahorrado ${encontrado['Dineroactual']} de ${encontrado['Dinerorequerido']}"
                            )
                            if encontrado["Dineroactual"] >= encontrado["Dinerorequerido"]:
                                print("¡Felicidades! Ya alcanzaste o superaste tu meta de ahorro.")
                            time.sleep(1)
                            mensajesaliendo()
                            break
                        else:
                            print("Solo puede ingresar numeros positivos")
            else:
                print(
                    "Este estudiante no tiene una meta de ahorro registrada. Cree una meta primero en la opción 3."
                )
        else:
            print("Este estudiante no existe, pruebe otro id")

    def eliminarahorro(self):
        existe = False
        with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
            estudiantes = json.load(archivo)["Registro"]
            print("Revisando registros...")
            time.sleep(1)
            for estudiante in estudiantes:
                if self.id == estudiante["id"]:
                    existe = True
                    seleccionado = estudiante
                    break
        if existe:
            encontrado = None
            for item in registroahorros:
                if item["id"] == seleccionado["id"]:
                    encontrado = item
                    break
            if encontrado and encontrado["Dineroactual"] > 0:
                print(
                    f"Meta: {encontrado['Meta']} | Dinero disponible en ahorros: ${encontrado['Dineroactual']}"
                )
                while True:
                    cant = input("¿Cuánto dinero desea retirar? (en $) >>> ").strip()
                    try:
                        cant = float(cant)
                    except ValueError:
                        print("Solo puede ingresar numeros positivos")
                    else:
                        if 0 < cant <= encontrado["Dineroactual"]:
                            anterior = encontrado["Dineroactual"]
                            encontrado["Dineroactual"] -= cant
                            with open(
                                "registroahorros.json", "w", encoding="utf-8"
                            ) as archivo:
                                json.dump(
                                    {"Ahorros": registroahorros},
                                    archivo,
                                    indent=2,
                                    ensure_ascii=False,
                                )
                            print(
                                f"Retiro exitoso. Tenías ${anterior} y retiraste ${cant}."
                            )
                            print(
                                f"Nuevo saldo en ahorros: ${encontrado['Dineroactual']} de ${encontrado['Dinerorequerido']}"
                            )
                            time.sleep(1)
                            mensajesaliendo()
                            break
                        else:
                            print(
                                "Cantidad invalida o mayor al dinero que tienes ahorrado"
                            )
            else:
                print("Este estudiante no tiene saldo disponible en ahorros para retirar")
        else:
            print("Este estudiante no existe, pruebe otro id")

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
