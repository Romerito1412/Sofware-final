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
        # 1. Leer el archivo de gastos
        try:
            with open("registrogastos.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                gastos_totales = datos.get("Gastos", [])
        except (FileNotFoundError, json.JSONDecodeError):
            print("No hay gastos registrados todavía.")
            return

        # 2. Buscar el registro del estudiante con el ID que se pasó
        registro_estudiante = None
        for reg in gastos_totales:
            if reg["id"] == self.id:
                registro_estudiante = reg
                break

        if not registro_estudiante:
            print(f"El estudiante con ID {self.id} no tiene gastos registrados.")
            return

        # 3. Mostrar qué gastos tiene actualmente
        print(f"\nGastos actuales del estudiante {self.id}:")
        areas = registro_estudiante["gastos"]
        hay_gastos = False
        for area, lista in areas.items():
            if lista:  # Si la lista no está vacía
                hay_gastos = True
                print(f" - {area}: {lista}")
        
        if not hay_gastos:
            print("Este estudiante no tiene ningún gasto registrado.")
            return

        # 4. Preguntar de qué área quiere eliminar
        while True:
            area_borrar = input("\n¿De qué área desea eliminar el gasto? (Comida/Transporte/Salidas/Estudios) >>> ").strip().title()
            
            if area_borrar not in areas:
                print("Área no válida. Intente de nuevo.")
                continue
            
            if not areas[area_borrar]:
                print(f"No hay gastos en {area_borrar}.")
                continue
                
            break # Si el área es válida y tiene gastos, salimos del bucle

        # 5. Mostrar los gastos de esa área numerados
        print(f"\nGastos en {area_borrar}:")
        for i, monto in enumerate(areas[area_borrar]):
            print(f" {i}. ${monto}")

        # 6. Pedir el número del gasto a eliminar y borrarlo
        while True:
            opcion = input("Ingrese el número del gasto a eliminar >>> ").strip()
            
            if opcion.isdigit() and 0 <= int(opcion) < len(areas[area_borrar]):
                posicion = int(opcion)
                eliminado = areas[area_borrar].pop(posicion)  # Aquí se borra
                print(f"\nSe eliminó el gasto de ${eliminado} en {area_borrar}.")
                break
            else:
                print("Número inválido. Intente de nuevo.")

        # 7. Guardar los cambios en el archivo .json
        with open("registrogastos.json", "w", encoding="utf-8") as archivo:
            json.dump({"Gastos": gastos_totales}, archivo, indent=2, ensure_ascii=False)

        print("Guardando cambios...")
        time.sleep(1)
        mensajesaliendo()
        
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
