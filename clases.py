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
                else:
                    existe = False
            if existe:
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
                                                "Transporte": [],
                                                "Salidas": [],
                                                "Estudios": [],
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
                                    break
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

            elif existe == False:
                "Este estudiante no existe, pruebe otro id"

    def eliminargasto(self):
        #El json.load está traduciendo registrosgastos y guardando el diccionario
        #En gastos_totales se va a buscar "Gastos"
        #Se pone [] porque eso hace que no de problemas el for 
        try:
            with open("registrogastos.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                gastos_totales = datos.get("Gastos", [])
                
        #Si el archivo no existe o no sirve se termina la función
        except (FileNotFoundError, json.JSONDecodeError):
            print("No hay gastos registrados todavía.")
            return

        #registro_estudiante es una variable vacía, temporalmente, es como Falso
        #el for recorre lo de gastos_totales que es "Gastos", o []
        #se compara el id del archivo con el id que ingresó en menú
        registro_estudiante = None
        for reg in gastos_totales:
            if reg["id"] == self.id:
                registro_estudiante = reg
                break
            
        #Para cuando el estudiante no está en la lista, es como si fuera Falso
        #Si no es verdad que hay datos en registro_estudiante
        if not registro_estudiante:
            print(f"El estudiante con ID {self.id} no tiene gastos registrados.")
            return

        #Mostrar qué gastos tiene actualmente
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

        #Preguntar de qué área quiere eliminar
        while True:
            area_borrar = input("\n¿De qué área desea eliminar el gasto? (Comida/Transporte/Salidas/Estudios): ").strip().title()
            
            if area_borrar not in areas:
                print("Área no válida. Intente de nuevo.")
                continue
            
            if not areas[area_borrar]:
                print(f"No hay gastos en {area_borrar}.")
                continue
                
            break #Si el área es válida y tiene gastos, salimos del bucle

        #La posición del gasto
        #enumerate es como range(len(gastos)
        print(f"\nGastos en {area_borrar}:")
        for i, monto in enumerate(areas[area_borrar]):
            print(f" {i}. ${monto}")

        #Pedir el número del gasto a eliminar y borrarlo
        while True:
            opcion = input("Ingrese el número del gasto a eliminar >>> ").strip()
            
            if opcion.isdigit() and 0 <= int(opcion) < len(areas[area_borrar]):
                posicion = int(opcion)
                eliminado = areas[area_borrar].pop(posicion)  # Aquí se borra
                print(f"\nSe eliminó el gasto de ${eliminado} en {area_borrar}.")
                break
            else:
                print("Número inválido. Intente de nuevo.")

        #Guardar los cambios en el archivo .json
        with open("registrogastos.json", "w", encoding="utf-8") as archivo:
            json.dump({"Gastos": gastos_totales}, archivo, indent=2, ensure_ascii=False)

        print("Guardando cambios...")
        time.sleep(1)
        mensajesaliendo()

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
