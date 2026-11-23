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
        existe = "noseguir"  # variable creada para definir si la persona debe seguir el proceso o no
        try:
            with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
                estudiantes = json.load(archivo)["Registro"]
        except (FileNotFoundError, json.JSONDecodeError):
            print("No hay estudiantes registrados.")
            return

        print("Revisando registros...")
        time.sleep(1)
        for estudiante in estudiantes:
            if self.id == estudiante["id"]:
                existe = "siguiente"  # si el estudiante existe la persona puede seguir, sino se le preguntara si quiere agregar otro id
                seleccionado = (
                    estudiante  # se guarda la informaciòn de la persona si  existe
                )

        if existe == "siguiente":
            print(
                f"Ha elegido al estudiante {seleccionado['nombre'].title()} con el ID {seleccionado['id']}"
            )
            time.sleep(1)
            activo = True
            while activo:
                print("¿En cuál área quiere registrar el gasto? (seleccione el número)")
                contador = 0
                for (
                    area
                ) in self.gastosregistro:  # se le muestran las 4 opciones existentes
                    contador += 1
                    print(f"{contador}. {area}")
                decision = input("Area >>> ").strip()
                if decision == "1":
                    # funcione si que sirve para ingresar el id, el area de gasto y la cantidad gastada para guardarla
                    activo = agregargastoarea(seleccionado, registro, "Comida")
                elif decision == "2":
                    # funcione si que sirve para ingresar el id, el area de gasto y la cantidad gastada para guardarla
                    activo = agregargastoarea(seleccionado, registro, "Transporte")
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
                    print("Esa opción no existe, pruebe otra")
                    continue
        else:
            print("Este estudiante no existe, pruebe otro id.")
            time.sleep(1)

    def eliminargasto(self):
        # 1. Leer el archivo de gastos
        try:
            with open("registrogastos.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                gastos_totales = datos.get("Gastos", [])
        except (FileNotFoundError, json.JSONDecodeError):
            print("  -No hay gastos registrados todavía.")
            time.sleep(1.5)
            return

        # 2. Verificar que el estudiante exista
        try:
            with open("registroestudiantes.json", "r", encoding="utf-8") as archivo:
                estudiantes = json.load(archivo)["Registro"]
        except (FileNotFoundError, json.JSONDecodeError):
            print("  -No hay estudiantes registrados.")
            time.sleep(1.5)
            return

        estudiante = None
        for est in estudiantes:
            if est["id"] == self.id:
                estudiante = est
                break

        if not estudiante:
            print(f"  -El estudiante con ID {self.id} no existe.")
            time.sleep(1.5)
            return

        print(f"\nEstudiante: {estudiante['nombre'].title()} (ID: {estudiante['id']})")

        # 3. Recolectar TODOS los gastos del estudiante (pueden estar en varios registros)
        gastos_por_area = {
            "Comida": [],
            "Transporte": [],
            "Salidas": [],
            "Estudios": [],
        }

        for reg in gastos_totales:
            if reg["id"] == self.id:
                for area, montos in reg["gastos"].items():
                    if area in gastos_por_area:
                        gastos_por_area[area].extend(montos)

        # 4. Mostrar qué gastos tiene actualmente
        hay_gastos = False
        print(f"\nGastos actuales del estudiante {self.id}:")
        for area, lista in gastos_por_area.items():
            if lista:
                hay_gastos = True
                print(f" - {area}: {lista}")

        if not hay_gastos:
            print("  -Este estudiante no tiene ningún gasto registrado.")
            time.sleep(1.5)
            return

        # 5. Preguntar de qué área quiere eliminar
        while True:
            area_borrar = (
                input(
                    "\n¿De qué área desea eliminar el gasto? (Comida/Transporte/Salidas/Estudios o 'salir') >>> "
                )
                .strip()
                .title()
            )

            if area_borrar.lower() == "salir":
                print("Cancelando eliminación...")
                return

            if area_borrar not in gastos_por_area:
                print("Área no válida. Intente de nuevo.")
                continue

            if not gastos_por_area[area_borrar]:
                print(f"No hay gastos en {area_borrar}.")
                continue

            break

        # 6. Mostrar los gastos de esa área numerados
        print(f"\nGastos en {area_borrar}:")
        for i, monto in enumerate(gastos_por_area[area_borrar]):
            print(f" {i + 1}. ${monto}")

        # 7. Pedir el número del gasto a eliminar
        while True:
            opcion = input(
                "Ingrese el número del gasto a eliminar (o 'salir') >>> "
            ).strip()

            if opcion.lower() == "salir":
                print("Cancelando eliminación...")
                return

            if opcion.isdigit() and 0 <= int(opcion) < len(
                gastos_por_area[area_borrar]
            ):
                posicion = int(opcion)
                monto_eliminado = gastos_por_area[area_borrar][posicion]
                break
            else:
                print("Número inválido. Intente de nuevo.")

        # 8. Eliminar el monto del archivo JSON original
        eliminado = False
        nuevos_gastos_totales = []

        for reg in gastos_totales:
            if reg["id"] == self.id and area_borrar in reg["gastos"]:
                if monto_eliminado in reg["gastos"][area_borrar] and not eliminado:
                    reg["gastos"][area_borrar].remove(monto_eliminado)
                    eliminado = True
                    # Si la lista queda vacía, quitamos esa área del registro
                    if not reg["gastos"][area_borrar]:
                        del reg["gastos"][area_borrar]
                    # Si el registro quedó sin áreas, no lo agregamos a la lista final
                    if reg["gastos"]:
                        nuevos_gastos_totales.append(reg)
                else:
                    nuevos_gastos_totales.append(reg)
            else:
                nuevos_gastos_totales.append(reg)

        if not eliminado:
            print("  -No se pudo eliminar el gasto (no se encontró en el archivo).")
            time.sleep(1.5)
            return

        # 9. Guardar cambios
        with open("registrogastos.json", "w", encoding="utf-8") as archivo:
            json.dump(
                {"Gastos": nuevos_gastos_totales}, archivo, indent=2, ensure_ascii=False
            )

        print(f"\nSe eliminó el gasto de ${monto_eliminado} en {area_borrar}.")
        print("Guardando cambios...")
        time.sleep(1.5)

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
<<<<<<< HEAD
                meta = input("¿Por qué está ahorrando? (Nombre de la meta) >>> ").strip()
                if meta == "":
                    print("Necesita llenar este campo")
                    continue
=======
                meta = input(
                    "¿Por qué está ahorrando? (Nombre de la meta) >>> "
                ).strip()
>>>>>>> 567ae5e9d0da7f465007c4dbd59554af37352a5b
                cant = input(
                    "Cantidad de dinero que quisiera ahorrar (en $) >>> "
                ).strip()
                try:
                    cant = float(cant)
                except ValueError:
                    print("  -Solo puede ingresar numeros positivos")
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
                        print("Datos no válidos, vuelva a intentar")
        else:
            print("  -Este estudiante no existe, pruebe otro id")
            time.sleep(1)

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
                    cant = input(
                        "¿Cuánto dinero deseas ingresar a tu ahorro? (en $) >>> "
                    ).strip()
                    try:
                        cant = float(cant)
                    except ValueError:
                        print("  -Solo puede ingresar numeros positivos")
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
                            print(f"Antes tenías ${anterior} y agregaste ${cant}.")
                            print(
                                f"Llevas ahorrado ${encontrado['Dineroactual']} de ${encontrado['Dinerorequerido']}"
                            )
                            if (
                                encontrado["Dineroactual"]
                                >= encontrado["Dinerorequerido"]
                            ):
                                print(
                                    "\n  -¡Felicidades! Ya alcanzaste o superaste tu meta de ahorro.\n"
                                )
                            time.sleep(1)
                            mensajesaliendo()
                            break
                        else:
                            print("  -Solo puede ingresar numeros positivos")
            else:
                print("\n")
                print(
                    "  -Este estudiante no tiene una meta de ahorro registrada. Cree una meta primero en la opción 3."
                )
                time.sleep(1)
        else:
            print("\n")
            print("  -Este estudiante no existe, pruebe otro id")
            time.sleep(1)

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
                        print("  -Solo puede ingresar numeros positivos")
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
                                f"\n  -Nuevo saldo en ahorros: ${encontrado['Dineroactual']} de ${encontrado['Dinerorequerido']}\n"
                            )
                            time.sleep(1)
                            mensajesaliendo()
                            break
                        else:
                            print("\n")
                            print(
                                "Cantidad inválida o mayor al dinero que tienes ahorrado"
                            )
                            time.sleep(1.5)
            else:
                print(
                    "  -Este estudiante no tiene saldo disponible en ahorros para retirar"
                )
                time.sleep(1)
        else:
            print("  -Este estudiante no existe, pruebe otro id")
            time.sleep(1)
