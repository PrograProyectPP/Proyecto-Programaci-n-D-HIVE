import os


ARCHIVO = "impresoras.txt"


impresoras = [
    ["Ultimaker 1", "LIBRE", ""],
    ["Ultimaker 2", "LIBRE", ""],
    ["Ultimaker 3", "LIBRE", ""],
    ["Ultimaker 4", "LIBRE", ""],
    ["Bambu Lab", "LIBRE", ""],
    ["Creativity", "LIBRE", ""]
]

def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for imp in impresoras:
            f.write(",".join(imp) + "\n")

def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            lineas = f.readlines()
            for i in range(len(lineas)):
                impresoras[i] = lineas[i].strip().split(",")

# --- Programa principal ---
cargar_datos()  # cargar si ya existe archivo

while True:
    print("\n=== Sistema de Impresoras 3D D-HIVE ===")
    print("1. Ver estado de impresoras")
    print("2. Solicitar impresora")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        for imp in impresoras:
            if imp[1] == "LIBRE":
                print(imp[0], ": DISPONIBLE")
            else:
                # 🔹 Mostrar solo usuario, no el código
                print(imp[0], ": OCUPADA por", imp[1])

    elif opcion == "2":
        nombre = input("Ingrese su número de carné: ")
        print("\nImpresoras disponibles:")
        libres = []
        for i in range(len(impresoras)):
            if impresoras[i][1] == "LIBRE":
                libres.append(i)
                print(len(libres), ".", impresoras[i][0])

        if len(libres) == 0:
            print("No hay impresoras libres")
        else:
            try:
                eleccion = int(input("Seleccione el número de impresora: ")) - 1
                if 0 <= eleccion < len(libres):
                    idx = libres[eleccion]

                    if impresoras[idx][1] != "LIBRE":  # Verificar si está ocupada
                        print("⚠️ La impresora seleccionada no está disponible.")
                    else:
                        codigo = str((idx+1)*1111)
                        impresoras[idx][1] = nombre
                        impresoras[idx][2] = codigo
                        guardar_datos()  # guardar cambios
                        print("✅ Asignada", impresoras[idx][0], "a", nombre, "con código", codigo)
                else:
                    print("⚠️ Número de impresora inválido.")
            except ValueError:
                print("⚠️ Debe ingresar un número válido.")

    elif opcion == "3":
        print("Saliendo del sistema... ¡Hasta pronto!")
        guardar_datos()
        break

    else:
        print("⚠️ Opción no válida, intente de nuevo.")
